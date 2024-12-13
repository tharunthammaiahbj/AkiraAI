from akiraai.utils.clean_up_html import cleanup_html
from akiraai.utils.clean_up_html import reduce_html




def main():

    
    base_url = "https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers"


    with open("/workspaces/AkiraAI/tests/html_samples/amazon/output1.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    
    try:
        title, minimized_body, link_urls, image_urls = cleanup_html(html_content,base_url)

        print("Title of the page: ")
        print(title)

        print("\nMinimised body content : ")
        print(minimized_body)

        print("\nLinks Found : ")
        print(link_urls)

        print("\nImages found:")
        for img in image_urls:
            print(img)

    except ValueError as e:
        print(f"Error during HTML cleanup: {e}")


    reduction_level = 1

    reduced_html = reduce_html(html=html_content, reduction=reduction_level)

    print("\nReduced HTML content:")
    print(reduced_html)


    reduced_file = "reduced.html"

    with open(reduced_file,"w",encoding="utf-8") as file:
        file.write(reduced_html)

    print(f"\nReduced HTML content saved to {reduced_file}")

main()


