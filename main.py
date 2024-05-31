import Scraper.scraper as SCR
import Model.model as model



if __name__ == "__main__":
    scraper = SCR.scraper("https://r.jina.ai/")
    # reader_api_result = scraper.fetch_reader_page("https://www.poewiki.net/wiki/Path_of_Exile_Wiki")
    
    # raw_html = scraper.fetch_raw_html("https://www.poewiki.net/wiki/Path_of_Exile_Wiki")
    # links_arr = scraper.html_extract_a(raw_html.content,"wiki.")
    prompt = "your name is Aiii a Path of exile wiki"
    ai_bot = model.Chatgpt(chatgpt_key,"gpt-4o",prompt,250,[{}])
    print(ai_bot.conversation("who u create with ? "))
        
    
    
    
    