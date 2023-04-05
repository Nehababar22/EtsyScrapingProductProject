import csv
import requests
from bs4 import BeautifulSoup


def main():
    """ 
    Etsy Product Information Scraping Script 
    """
    
    # Writing Header for Output File
    with open("output.csv", "a", newline='') as output_file:
        writer = csv.writer(output_file) 
        header = ['Product Link','Not in Stock?','Title & Author','Shipping Time','Price',
        'Description','Store','Categories','Created','Country Of Origin','Image Link'] 
        writer.writerow(header)

    # Reading Input file
    with open('/home/neha/EtsyProject/input.csv','r') as input_file:
       
        # Iterate Over rows from Input file
        for url in input_file:
            response = requests.get(url) 
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.find_all('div',class_='wt-pt-xs-5 listing-page-content-container-wider wt-horizontal-center')

            #Create results as empty list   
            results = []
        
            #Scraping data from each urls   
            for product in data:          
                productlink= url.rstrip()
                notinstock = soup.find('span',class_='wt-icon wt-icon--smaller').text.strip()
                titleandauthor = soup.find('h1',class_='wt-text-body-03 wt-line-height-tight wt-break-word').text.strip()
                shippingtime= soup.find('p',class_='wt-text-body-03 wt-mt-xs-1 wt-line-height-tight').text
                price= soup.find('p',class_='wt-text-title-03 wt-mr-xs-2').text.strip()
                description= soup.find('p',class_='wt-text-body-01 wt-break-word').text.strip()
                store= soup.find('p',class_='wt-text-body-01 wt-mr-xs-1').text.strip()
                categories= soup.find('div',id='wt-content-toggle-tags-read-more').get_text(strip=True,separator=" ")
                created= soup.find('div',class_='wt-pr-xs-2 wt-text-caption').text.strip()
                countryoforigin= soup.find('div',class_='wt-grid__item-xs-12 wt-text-black wt-text-caption').text.strip()
                imagelink = soup.find_all('div', {'class': 'image-carousel-container wt-position-relative wt-flex-xs-6 wt-order-xs-2 show-scrollable-thumbnails'})
                if imagelink:
                    img = imagelink[0].find('img')['src']
                datas = [productlink,notinstock,titleandauthor,shippingtime,price,description,store,categories,created,countryoforigin,img]                
                results.append(datas)
                    
               # The scraped info will be written to a output file here.
                with open("output.csv", "a", newline='') as output_file:
                    writer = csv.writer(output_file) 
                    writer.writerows(results)


if __name__ == "__main__":
    main()
