import os
import openai
from PIL import Image
import streamlit as st
from fpdf import FPDF
import base64
import tweepy
import pyperclip

st.set_option('deprecation.showfileUploaderEncoding', False)

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

st.set_page_config(
    page_title="STEM-FRND",
    page_icon="",
    layout="wide",
    initial_sidebar_state="auto",
)


openai.api_key = "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"

@st.cache_data(persist=True, show_spinner=False)
def openai_completion(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=1
    )
    return response['choices'][0]['text']

@st.cache_data(persist=True, show_spinner=False)
def tweek(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        temperature=1
    )
    return response['choices'][0]['text']

@st.cache_data(persist=True, show_spinner=False)
def blogpost(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        temperature=1
    )
    return response['choices'][0]['text']

@st.cache_data(persist=True, show_spinner=False)
def prompt(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        temperature=1
    )
    return response['choices'][0]['text']

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def openai_image(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url

def story(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url

def comic(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url
top_image = Image.open('static/banner_top.png')

st.sidebar.image(top_image,use_column_width='auto')
with st.sidebar:
    st.write("Generate Tweet: Generates tweet based on info displayed in textbox.       \n        Generate Image: Develops optionally AI queried image to help illustrate concept.            \n                        Generate Blog Post: Produces blog post explaining topic in detail and search engine optimized.                    \n  Generate DALL-E: Develops query to best illustrate concept when entered into DALL-E via AI.")


st.markdown("<h1 style='text-align: center; color: blue;'>STEM-FRND</h1>", unsafe_allow_html=True)

input_text = st.text_area("What should I write about?",height=50)
tweet_pressed = st.button("Generate Tweet")
if tweet_pressed:
    tweek1 = tweek("write a tweet" + input_text)
    st.success(tweek1)

blog_pressed = st.button("Generate Blog")
if blog_pressed:
    blogpost1 = blogpost("create a blog post that is in depth and SEO optimized, do not use em dashes" + input_text)
    st.success(blogpost1)

prompt_pressed = st.button("Generate Dall-E Prompt")
if prompt_pressed:
    prompt1 = prompt("create a prompt for Dall-E to generate an image using this input, and do not mention Dall-E in your response, but do mention the original input" + input_text)
    st.success(prompt1)
    pyperclip.copy(prompt1)
spam = pyperclip.paste()

education_pressed = st.button("Generate Education Article")
if education_pressed:
    education1 = openai_completion(input_text)
    st.success(education1)

input_text = st.text_area("What should I draw?", spam ,height=50,)
image_button = st.button("Generate Custom Image")
if image_button:
    image_url = openai_image(input_text)
    st.image(image_url, caption='Courtesy of Charlie, your STEM-FRND')

cgi_button = st.button("Generate 3D Image")
if cgi_button:
    story1 = story("Give me a 3d render" + input_text)
    st.image(story1, caption='Courtesy of Charlie, your STEM-FRND')

comic_button = st.button("Generate Comic-Book-Style art")
if comic_button:
    comic1 = comic("Draw in comic book art syle, with popping colors" + input_text)
    st.image(comic1, caption='Courtesy of Charlie, your Amazing STEM-FRND')


report_text = st.text_input("Report Text")


export_as_pdf = st.button("Export Report")

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

if export_as_pdf:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(180, 10, report_text)
    
    
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

    st.markdown(html, unsafe_allow_html=True)

export_as_tweet = st.button("Tweet it!")

if export_as_tweet:
    st.text("Done")

export_as_insta = st.button("Post it!")

if export_as_insta:
    st.text("Done")