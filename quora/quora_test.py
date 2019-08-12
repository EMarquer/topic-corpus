import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()

# driver = webdriver.Firefox()
driver.get("https://www.quora.com/topic/Cooking")
time.sleep(1)
elem = driver.find_element_by_tag_name("body")
no_of_pagedowns = 7
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1
post_elems =driver.find_elements_by_xpath("//a[@class='question_link']")
for post in post_elems:
    answer_texts = []
    questions = post.find_element(By.CSS_SELECTOR, ".ui_qtext_rendered_qtext")

    # print(questions.text)

    parents = post.find_elements_by_xpath("ancestor::div[@class='story_title_container']")
    for parent in parents:
        print(parent.text, 'this is a parent text print')
        answer_bodies = parent.find_elements_by_xpath("following-sibling::div[@class='Answer']")
        # print(answer_body.text)
        for answer_body in answer_bodies:
            print('answer_body:', answer_body.text)
            # answer_expandable = answer_body.find_elements_by_xpath("descendant::div[@class='Expandable SimpleToggle Toggle AnswerExpandable AnswerInFeedExpandable']")
            answer_preview = answer_body.find_elements(By.CSS_SELECTOR, ".answer_body_preview")
            # print(answer_preview.text)

            # answer_hidden = answer_body.find_elements_by_xpath("descendant::div[@class='Expandable SimpleToggle Toggle AnswerExpandable AnswerInFeedExpandable hidden']")
            for prev in answer_preview:
                answer_texts = prev.find_elements(By.CSS_SELECTOR, ".ui_qtext_rendered_qtext") #ui_qtext_para u-ltr u-text-align--start ## doesn't work

                # anwer_texts = answer.find_elements_by_xpath("descendant::p[@class='ui_qtext_rendered_qtext']")
                for ans in answer_texts:
                    print('answers:', ans.text)
    # hidden_answer_texts =

    print('\n'*3)
