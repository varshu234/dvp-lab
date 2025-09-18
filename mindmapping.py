import matplotlib.pyplot as plt
import networkx as nx
import speech_recognition as sr
from graphviz import Digraph
import math
import os
import numpy as np
from duckduckgo_search import DDGS
from PIL import Image
import requests
from io import BytesIO
import random

# ----------- VOICE INPUT FUNCTION ------------
def get_voice_input(prompt_text="Speak now..."):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"🎤 {prompt_text}")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ Recognized: {text}")
        return text
    except:
        print("⚠️ Voice input failed.")
        return ""

# ----------- IMAGE SEARCH FUNCTIONS ------------
def search_images_online(query, max_images=3):
    urls = []
    with DDGS() as ddgs:
        for result in ddgs.images(query, max_results=max_images):
            urls.append(result["image"])
    return urls

def show_images_from_urls(urls, topic):
    for i, url in enumerate(urls):
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img.show()
            img.save(f"{topic}_image_{i+1}.png")
            print(f"✅ Image {i+1} saved as '{topic}_image_{i+1}.png'")
        except:
            print(f"⚠️ Failed to load image {i+1}")

# ----------- PREVIEW FUNCTIONS ------------
def preview_layout(title):
    urls = search_images_online(title + " layout diagram", max_images=1)
    if urls:
        print(f"📷 Preview for {title} layout")
        show_images_from_urls(urls, title.replace(" ", "_"))
    else:
        print(f"❌ No preview found for {title} layout")

# ----------- MIND MAP DRAWING FUNCTIONS ------------
def random_color():
    return ["skyblue", "lightgreen", "lightcoral", "orange", "lightpink", "khaki"][random.randint(0, 5)]

def create_bubble(main, subtopics):
    G = nx.DiGraph()
    G.add_node(main)
    for sub in subtopics:
        G.add_edge(main, sub)
    plt.figure(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_size=2500, node_color=random_color(), font_weight='bold')
    plt.title(f"Bubble Mind Map for: {main}\nSubtopics: {', '.join(subtopics)}")
    plt.show()

def create_tree(main, subtopics):
    dot = Digraph()
    dot.node('A', main)
    for i, sub in enumerate(subtopics):
        dot.node(f"B{i}", sub)
        dot.edge('A', f"B{i}")
    print(f"Tree Layout: {main} -> {', '.join(subtopics)}")
    dot.render("tree_map", view=True, format="png")

def create_radial(main, subtopics):
    G = nx.Graph()
    G.add_edges_from([(main, t) for t in subtopics])
    pos = nx.shell_layout(G, [[main], subtopics])
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color=random_color(), node_size=2000, font_weight='bold')
    plt.title(f"Radial Mind Map for: {main}\nSubtopics: {', '.join(subtopics)}")
    plt.show()

def create_spiral(main, subtopics):
    fig, ax = plt.subplots()
    ax.text(0, 0, main, fontsize=14, ha='center')
    for i, topic in enumerate(subtopics):
        angle = 0.5 * i
        x = angle * math.cos(angle)
        y = angle * math.sin(angle)
        ax.plot([0, x], [0, y], linestyle='--', color='gray')
        ax.text(x, y, topic, fontsize=12, ha='center')
    ax.set_title(f"Spiral Mind Map for: {main}\nSubtopics: {', '.join(subtopics)}")
    ax.axis('off')
    plt.show()

def create_fishbone(main, subtopics):
    fig, ax = plt.subplots()
    ax.plot([0, 10], [0, 0], color='black')  # main line
    for i, sub in enumerate(subtopics):
        direction = 1 if i % 2 == 0 else -1
        x = 1 + i
        ax.plot([x, x - 0.5], [0, direction], color='gray')
        ax.text(x - 0.5, direction + 0.2 * direction, sub, ha='center')
    ax.text(10.5, 0, main, fontsize=12, ha='left')
    ax.set_title(f"Fishbone Mind Map for: {main}\nSubtopics: {', '.join(subtopics)}")
    ax.axis('off')
    plt.show()

# ----------- MAIN FUNCTION ENTRY POINT ------------
if __name__ == "__main__":
    print("🎯 Welcome to the Advanced Mind Map + Visual Generator")

    method = input("Choose input method (text/voice): ").strip().lower()

    if method == "voice":
        main_topic = get_voice_input("Speak main topic")
    else:
        main_topic = input("Enter main topic: ")

    n = int(input("How many subtopics? "))
    subtopics = []
    for i in range(n):
        if method == "voice":
            sub = get_voice_input(f"Speak subtopic {i+1}")
        else:
            sub = input(f"Enter subtopic {i+1}: ")
        subtopics.append(sub)

    # Detect math-related topic
    if any(word in main_topic.lower() for word in ["trig", "math", "graph", "sin", "cos", "tan"]):
        print("📈 Math topic detected. Fetching graph...")
        urls = search_images_online(main_topic + " graph", max_images=1)
        show_images_from_urls(urls, main_topic.replace(" ", "_") + "_graph")

    # Detect biology/science topic
    if any(word in main_topic.lower() for word in ["respiratory", "lungs", "photosynthesis", "digestive"]):
        print("🔍 Science topic detected. Fetching diagram...")
        urls = search_images_online(main_topic + " diagram", max_images=1)
        show_images_from_urls(urls, main_topic.replace(" ", "_") + "_diagram")

    print("\n🎨 Choose layout:")
    print("1. Bubble")
    print("2. Tree")
    print("3. Radial")
    print("4. Spiral")
    print("5. Fishbone")
    layout = input("Enter number: ").strip()

    print(f"\n📋 Main Topic: {main_topic}")
    print(f"📌 Subtopics using layout: {', '.join(subtopics)}")
    preview_layout(main_topic + " layout")

    if layout == "1":
        create_bubble(main_topic, subtopics)
    elif layout == "2":
        create_tree(main_topic, subtopics)
    elif layout == "3":
        create_radial(main_topic, subtopics)
    elif layout == "4":
        create_spiral(main_topic, subtopics)
    elif layout == "5":
        create_fishbone(main_topic, subtopics)
    else:
        print("❌ Invalid layout choice.")
