from getInfo import get_site_info

item = {
    "img": "https://images.kabum.com.br/produtos/fotos/393218/notebook-asus-vivobook-15-amd-ryzen-5-4600h-8gb-ram-ssd-256gb-15-6-full-hd-amd-radeon-graphics-win-11-prata-metalico-m1502ia-ej251w_1710269786_gg.jpg",
    "title": "Notebook ASUS Vivobook 15 AMD Ryzen 5-4600H",
    "details": "8GB RAM, SSD 256GB, 15.6 Full HD, AMD Radeon Graphics, Win 11, Prata Metálico",
    "serial": "M1502IA-EJ251W",
    "links": [
        {
            "_id": "611f7b3b7f3b3b1b3c7f3b3b",
            "name": "kabum",
            "url": "https://www.kabum.com.br/produto/393218/",
            "actualPrice": "R$ 5.999,00",
            "actualPriceCreditCard": "R$ 5.999,00",
            "bestPrice": "R$ 5.999,00",
            "bestPriceDate": "2021-08-24",
            "actualPriceDate": "2021-08-24",
        },
        {
            "_id": "611f7b3b7f3b3b1b3c7f3b3c",
            "name": "amazon",
            "url": "https://www.amazon.com.br/dp/B0BFVR41MY",
            "actualPrice": "R$ 5.999,00",
            "actualPriceCreditCard": "R$ 5.999,00",
            "bestPrice": "R$ 5.999,00",
            "bestPriceDate": "2021-08-24",
            "actualPriceDate": "2021-08-24",
        },
        {
            "_id": "611f7b3b7f3b3b1b3c7f3b3d",
            "name": "mercado_livre",
            "url": "https://www.mercadolivre.com.br/p/MLB22384462",
            "actualPrice": "R$ 5.999,00",
            "actualPriceCreditCard": "R$ 5.999,00",
            "bestPrice": "R$ 5.999,00",
            "bestPriceDate": "2021-08-24",
            "actualPriceDate": "2021-08-24",
        },
        {
            "_id": "611f7b3b7f3b3b1b3c7f3b3e",
            "name": "fast_shop",
            "url": "https://www.fastshop.com.br/web/p/d/3002284704_PRD/notebook-asus-vivobook-m1502ia-ej251w-ryzen-5-8gb-256gb-ssd-windows-11-home-1560quot-full-hd",
            "actualPrice": "R$ 5.999,00",
            "actualPriceCreditCard": "R$ 5.999,00",
            "bestPrice": "R$ 5.999,00",
            "bestPriceDate": "2021-08-24",
            "actualPriceDate": "2021-08-24",
        }
        
    ],
}


def get_all_info():
    for link in item["links"]:
        get_site_info(link)


if __name__ == "__main__":
    get_all_info()
