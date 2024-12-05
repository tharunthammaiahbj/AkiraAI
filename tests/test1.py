"""
Test for Scrape_do module
"""
from akiraai.web_doc_loader.scrape_do import scrape_do_fetch  # Replace with your module name

def test_scrape_do():
    token = "930002fa47f249da87613f0555eefad972d6bc934aa"  # Replace with your API token
    target_url = "https://sale.alibaba.com/p/rank/list.html?spm=a2700.product_home_newuser.scenario_overview.topRanking&wx_navbar_transparent=true"  # Example URL for testing

    # Test with residential proxy
    print("Testing with residential proxy...")
    response = scrape_do_fetch(token, target_url, use_proxy=True, geoCode="US", super_proxy=True)
    print("Response with residential proxy:", response)
    

if __name__ == "__main__":
    test_scrape_do()
