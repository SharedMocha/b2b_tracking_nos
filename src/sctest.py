"""
Developed by :SharedMocha
Developed on :05/28/2018
Code Reviewers : ******
FileName:sc.py
Usage:B2BTracking smart contract acts as base version to transfer asset (or) package information between various companies in a trusted way.
As an example when a customer orders a product at Amazon the information is sent to warehouse or depot.
The warehouse or depot then packages the product and hands the package to shipping company like Fedex which delivers it to customer.
Using this smart contract one can create,track,update,transfer an asset (or) package accordingly.
Pending Items : ******
Bugs : *******
"""

from boa.interop.Neo.Runtime import CheckWitness,Serialize,Deserialize
from boa.interop.Neo.Storage import GetContext, Put, Delete, Get
#import datetime
#from boa.builtins import concat


def is_owner(modifier_id,case_id):
    #Verify if the updater of an asset is one of the 3 participants(Created,Warehouse owner,Shipper).
    orderedby_company_hash = Get(GetContext(), orderedby_company_hash)
    shipping_company_depot_hash = Get(GetContext(), shipping_company_depot_hash)
    carrier_company_hash = Get(GetContext(), carrier_company_hash)
    if (orderedby_company_hash == modifier_id) or (shipping_company_depot_hash == modifier_id) or (carrier_company_hash == modifier_id):
        print("Requestor accepted")
        return True
    else:
        print("Required not valid ")
        return False


# Main Operation

def Main(operation, args):
    """
    Main definition for the smart contracts
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

    #Check if requestor is  valid
    requestor_hash = args[0]
    authorized_requestor = CheckWitness(requestor_hash)
    if not authorized_requestor:
        print("Requestor is Not Authorized")
        return False
    print("Requestor is Authorized")
    
    #Check if required params are present-Always accept all 14 params
    if len(args) < 13:
        print('Not all required parameters are passed')
        return False
    else:
        print('All required parameters are passed')
    
    #Capture param values
    case_id = 78
    ordered_by_name = args[2]
    orderedby_company_hash = args[3]
    shipping_company_depot_code = args[4]
    shipping_company_depot_hash = args[5]
    carrier_name = args[6]
    carrier_company_hash = args[7]
    product_id = args[8]
    quantity = args[9]
    customer_name = args[10]
    delivery_by = args[11]
    customer_address = args[12]
    arrayone = Serialize([ordered_by_name,orderedby_company_hash,shipping_company_depot_code,shipping_company_depot_hash,carrier_name,carrier_company_hash,product_id,quantity,customer_name,customer_address,delivery_by])

    # start operations
    #main code
    if operation != None:
        if operation == 'RegisterAsset':
            #Register Asset for sending to customer.This is invoked for companies like Amazon to send a product to customer
            print('About to Register Asset for shipment')
            asset_exists = Get(GetContext(), case_id)
            if not asset_exists:
                status = "New"
                Put(GetContext(), case_id,arrayone)
                print("Registered New Asset for shipment")
                return True

    if operation == 'TransferAssetToShipper':
        #After a warehouse receives an order it will pick it hand it over to shipping company like Fedex
        print('Transfer Asset from Warehouse or Depot to Shipper like Fedex')
        if is_owner(shipping_company_depot_hash,case_id):
            status = "Transferred"
            Put(GetContext(), case_id,arrayone)
            print("Product Transferred to Shipper")
            return True

    if operation == 'UpdateAssetInformation':
        #Shipping company like FedEx will update final status after product is delivered
        print('Product Shipped to customer')
        if is_owner(shipping_company_depot_hash,case_id):
            status = "Delivered"
            #date_time_delivered = datetime.datetime.now()
            print("Product Delivered to customer")
            Put(GetContext(), case_id,arrayone)
            return True
        
    if operation == 'GetStatusOfShipment':
        #Shipping company like FedEx will update final status after product is delivered
        print('Get status of shipment')
        status = Get(GetContext(), case_id)
        return status
    return False
