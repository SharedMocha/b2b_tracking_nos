# b2b_tracking_nos

Usage:B2BTracking smart contract acts as base version to transfer asset (or) package information between various companies in a trusted way.
As an example when a customer orders a product at Amazon the information is sent to warehouse or depot.
The warehouse or depot then packages the product and hands the package to shipping company like Fedex which delivers it to customer.
Using this smart contract one can create,track,update,transfer an asset (or) package accordingly.

    :operations this smart contract performs:
    RegisterAsset :To register a new asset that needs to sent to customer at some location via partners
    TransferAssetToShipper :Transfer asset from one party to another(From warehouse to shipper).
    UpdateAssetInformation :Update asset as it goes through various parties
    GetStatusOfShipment :Get current status of shipment
    
    :param args: global list of arguments.
        args[0] requestId
        args[1] casenumber
        args[2] ordered_by_name(Ex-Amazon)
        args[3] ordered_by_hash(Ex-Amazon)
        args[4] shipping_company_depot_code(Ex-Depot123 in London)
        args[5] shipping_company_depot_hash(Ex-Depot123 in London)
        args[6] carrier_name(Ex-FedEx,UPS,DHL)
        args[7] carrier_company_hash(Ex-FedEx,UPS,DHL)
        args[8] product_Id(Ex-123)
        args[9] quantity (Ex-10)
        args[10] customer_name (Ex-10)
        args[11] delivery_by_date_time (Ex- 12/01/2018 2:53 PM GMT)
        args[12] customer_address
    :param type: str and date
    :return:
        byterarray: The result of the operation
    """
