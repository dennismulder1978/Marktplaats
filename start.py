from marktplaats import SearchQuery

search = SearchQuery("Paiste", # Search query
                     zip_code="1341DC", # Zip code to base distance from
                     distance=0, # Max distance (meters) from the zip code for listings
                     price_from=0, # Lowest price to search for
                     price_to=100, # Highest price to search for
                     limit=5, # Max listings (page size, max 25)
                     offset=0) # Offset for listings (page * limit)

listings = search.get_listings()

for listing in listings:
    print(listing.title)
    # print(listing.description)
    print(listing.price)
    # print(listing.link)
    
    # # the location object
    # print(listing.location)
    
    # # the seller object
    # print(listing.seller)
    
    # # the datetime object
    # print(listing.date)
    
    # # the full seller object (another request)
    # print(listing.seller.get_seller())
    
    # for image in listing.images:
    #     print(image.medium)
    
    
    print("-----------------------------")