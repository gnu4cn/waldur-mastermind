from rest_framework.settings import api_settings
from rest_framework import test

from waldur_core.structure.tests import factories as structure_factories
from waldur_core.structure.tests import fixtures as structure_fixtures
from waldur_mastermind.invoices import models as invoice_models
from waldur_mastermind.invoices.tests import factories as invoice_factories

from .. import models


class CustomerEstimatedCostFilterTest(test.APITransactionTestCase):
    def setUp(self):
        models.PriceEstimate.objects.filter(scope=structure_factories.CustomerFactory()).update(total=200)
        models.PriceEstimate.objects.filter(scope=structure_factories.CustomerFactory()).update(total=100)
        models.PriceEstimate.objects.filter(scope=structure_factories.CustomerFactory()).update(total=300)
        structure_factories.CustomerFactory()

    def execute_request(self, ordering_param=None):
        fixture = structure_fixtures.CustomerFixture()
        url = structure_factories.CustomerFactory.get_list_url()

        self.client.force_login(fixture.staff)
        params = {}
        if ordering_param:
            params[api_settings.ORDERING_PARAM] = ordering_param
        response = self.client.get(url, params)

        return [int(customer['billing_price_estimate']['total']) for customer in response.data]

    def test_ascending_ordering(self):
        actual = self.execute_request('estimated_cost')
        self.assertEqual([0, 100, 200, 300], actual)

    def test_descending_ordering(self):
        actual = self.execute_request('-estimated_cost')
        self.assertEqual([300, 200, 100, 0], actual)

    def test_default_ordering(self):
        actual = self.execute_request()
        self.assertEqual([200, 100, 300, 0], actual)


class CustomerCurrentCostFilterTest(test.APITransactionTestCase):
    def setUp(self):
        for price in [200, 100, 300]:
            project = structure_factories.ProjectFactory()
            invoice = invoice_factories.InvoiceFactory(customer=project.customer)
            invoice_factories.GenericInvoiceItemFactory(
                invoice=invoice,
                project=project,
                unit_price=price,
                quantity=1,
                unit=invoice_models.GenericInvoiceItem.Units.QUANTITY
            )
        structure_factories.CustomerFactory()

    def execute_request(self, ordering_param=None):
        fixture = structure_fixtures.CustomerFixture()
        url = structure_factories.CustomerFactory.get_list_url()

        self.client.force_login(fixture.staff)
        params = {}
        if ordering_param:
            params[api_settings.ORDERING_PARAM] = ordering_param
        response = self.client.get(url, params)

        return [int(customer['billing_price_estimate']['current']) for customer in response.data]

    def test_ascending_ordering(self):
        actual = self.execute_request('current_cost')
        self.assertEqual([0, 100, 200, 300], actual)

    def test_descending_ordering(self):
        actual = self.execute_request('-current_cost')
        self.assertEqual([300, 200, 100, 0], actual)

    def test_default_ordering(self):
        actual = self.execute_request()
        self.assertEqual([200, 100, 300, 0], actual)
