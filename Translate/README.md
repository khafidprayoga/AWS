# About
Amazon Translate is a neural machine translation service for translating text to and from English across a breadth of supported languages. Powered by deep-learning technologies, Amazon Translate delivers fast, high-quality, and affordable language translation. It provides a managed, continually trained solution so you can easily translate company and user-authored content or build applications that require support across multiple languages. The machine translation engine has been trained on a wide variety of content across different domains to produce quality translations that serve any industry need.  

# How to Use  
1. Create IAM user (Programmatic access)   
2. Input your login identity at `~/.aws/credentials`   
    ```
    [default]
    aws_access_key_id = AAAAxxxxxxxxxx
    aws_secret_access_key = AAAAA+maVxxxxxxxxxxxxx
    ```
3. Navigate your directory at **AWS/Translate**
4. Create virtual environment  
    `python -m venv env`
5. Enable venv  
    `source env/bin/activate`
6. Install the component  
    `pip install --editable .`

Run: `translate --help`
