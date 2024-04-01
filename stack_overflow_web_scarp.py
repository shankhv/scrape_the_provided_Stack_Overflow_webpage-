import requests
from bs4 import BeautifulSoup

response = requests.get("https://notifications.googleapis.com/email/redirect?t=AFG8qyWvS5iZ5SlSKsQTXOBpvAkIOn2d-viNIXQsj_kdYuEvIb9SqhiJN5eooQrlGeSo0ErdSz2OLAbJoi94N6lOA60YvjQD9VRFMOwszZwXTJLkwl6B56MCwNbEQRBsZA4YBWvQXRf-Cpo0UocZfT1RtoYILwWWIUsFqWpq09EGC7xGGze3MM1JSGa4JUVFAEA4894XBJsvlPAAEivaSuf5T8OYp-XtrCSYnzzvGH-Pl8q2P4et7wtaRR2WQbv2eXLnXo_qrdlypO-IsYyszRVM9BPXFTKrptUO7jhtj9E6hyrm2HdpnurRxlDFTXSVPaOxCAImX3g&r=eJwNxlEOgCAIANATEXPLn27TjMKVYIK5bl_v67F7tQXRfE2nPtT2S8eUtODdyTyrGM4hxhCQdcCmkOEgB2eC1Fsj-Z8LQRaor7PKB-HdHgo&s=ALHZ2r7mFSgCHxSlCMgAqe4na2TJ")
if response.status_code == 200:
    result = response.text
    result = soup = BeautifulSoup(response.text, "html.parser")
    question_title = soup.title.get_text()

# Check if the title matches the specified question
    if "How do I get the current time in Python?" in question_title:
        # Find the question body
        question_body = soup.find("div", class_="question")

        # Extract the question text
        question_text = question_body.find("div", class_="s-prose js-post-body").get_text(strip=True)

        # Find all answers to the question
        answers = soup.find_all("div", class_="answer")

        # Extract the answer texts
        answer_texts = [answer.find("div", class_="s-prose js-post-body").get_text(strip=True) for answer in answers]

        print("Question:")
        print(question_text)
        print("\nAnswers:")
        for i, answer_text in enumerate(answer_texts, start=1):
            print(f"Answer {i}:")
            print(answer_text)
    else:
        print("Question not found.")
else:
    print("API IS NOT RESPONDING")