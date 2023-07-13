from abc import ABC, abstractmethod


class ShippingService(ABC):

    @abstractmethod
    def get_price_quote(self, item):
        raise NotImplemented()

    @abstractmethod
    def get_max_package_size(self):
        raise NotImplemented()


class UpsNationwideShipping(ShippingService):
    def get_price_quote(self, item):
        pass

    def get_max_package_size(self):
        pass

class UpsInternationalShipping(ShippingService):
    def get_price_quote(self, item):
        pass

    def get_max_package_size(self):
        pass

class UpsFreightShipping(ShippingService):
    def get_price_quote(self, item):
        pass

    def get_max_package_size(self):
        pass

class DhlOceanFreightShipping(ShippingService):
    def get_price_quote(self, item):
        pass

    def get_max_package_size(self):
        pass


class DhlAirFreightShipping(ShippingService):
    def get_price_quote(self, item):
        pass

    def get_max_package_size(self):
        pass


class ShippingServiceFactory(ABC):

    @abstractmethod
    def get_shipping_service(self,shipping_type: str):
        raise NotImplemented()

class UpsShippingServiceFactory(ShippingServiceFactory):

    mapping = {
        'nationwide': UpsNationwideShipping,
        'international': UpsInternationalShipping,
        'freight': UpsFreightShipping
    }

    def get_shipping_service(self, shipping_type: str):
        return UpsShippingServiceFactory.mapping[shipping_type]()

class DHLShippingServiceFactory(ShippingServiceFactory):

    mapping = {
        'ocean_freight': DhlOceanFreightShipping,
        'air_freight': DhlAirFreightShipping,
    }
    def get_shipping_service(self, shipping_type: str):
        return DHLShippingServiceFactory.mapping[shipping_type]()

class ShippingFactoryProvider:
    @staticmethod
    def get_shipping_factory(company_name):
        if company_name == 'DHL':
            return DHLShippingServiceFactory()
        else:
            return UpsShippingServiceFactory()


if __name__ == '__main__':
    # ShippingServiceFactory.get_shipping_service("nationwide")
    # DHLShippingServiceFactory().get_shipping_service("freight")
    # UpsShippingServiceFactory
    company_name = "DHL"
    service_type = 'air_freight'
    ShippingFactoryProvider\
        .get_shipping_factory(company_name)\
        .get_shipping_service(service_type)

# class Plot:
#     def __init__(self, label=False, grid=True, legend=True):
#         pass
#
# Plot().setLegend().setGrid().setLabels()
