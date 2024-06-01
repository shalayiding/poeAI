# Fetch Reader Page

```json
{
  "function": "fetch_reader_page",
  "description": "Extracting information from Webpage using URL",
  "parameters": {
    "type": "object",
    "properties": {
      "PAGE_URL": {
        "type": "string",
        "description": "URL of the webpage"
      }
    },
    "required": ["PAGE_URL"]
  }
}
```

# Fetch Raw HTML

```json
{
  "function": "fetch_raw_html",
  "description": "Extracting raw html from Webpage using URL",
  "parameters": {
    "type": "object",
    "properties": {
      "PAGE_URL": {
        "type": "string",
        "description": "URL of the webpage"
      }
    },
    "required": ["PAGE_URL"]
  }
}
```

# HTML Extract A

```json
{
  "function": "html_extract_a",
  "description": "Extracting all a tag in html with matching pattern from Webpage",
  "parameters": {
    "type": "object",
    "properties": {
      "PAGE_HTML": {
        "type": "string",
        "description": "HTML code in string of the website"
      },
      "Pattern": {
        "type": "string",
        "description": "The pattern that the algorithm is gonna search from"
      }
    },
    "required": ["PAGE_HTML", "Pattern"]
  }
}
```
