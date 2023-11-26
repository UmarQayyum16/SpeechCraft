import streamlit as st
from openai import OpenAI
from PIL import Image

# Retrieve the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Initialize OpenAI
client = OpenAI(api_key=openai_api_key)

# Declare global variables
global prompt
global tone
global target_audience
global purpose
global expected_duration
# Example user prompt
sample_user_prompt_1 = f"Generate a compelling presentation guidance on the topic of Innovations in Sustainable Energy. Set the tone to Inspirational for a Environmentalists and Engineers audience. The purpose is to To showcase groundbreaking innovations in sustainable energy, emphasizing their impact on the environment., and the expected duration is 40 minutes."

sample_user_prompt_2 = f"Generate a compelling presentation guidance on the topic of Effective Communication in Relationships. Set the tone to Empathy for a Couples and Individuals audience. The purpose is To explore the importance of communication in relationships and offer tips for fostering healthy and effective communication., and the expected duration is 35 minutes."
assistant_content_hook_1 = """
Catchy Hook:
"Imagine a world where our energy needs are met without harming the environment. A world where we harness the power of innovation to create sustainable solutions for our energy demands. Welcome, environmentalists and engineers, to a journey of inspiration and discovery as we explore the remarkable innovations in sustainable energy that are revolutionizing our planet. Today, we will delve into the groundbreaking technologies, explore their impact on the environment, and envision a future powered by clean and renewable energy."
"""

assistant_content_hook_2 = """
Engage the audience with a relatable and thought-provoking statement: "Have you ever felt like you were speaking a different language even though you were using the same words? We've all been there. Today, we will dive into the world of effective communication in relationships, and discover how empathy can be the key to creating stronger, more fulfilling connections."
"""
assistant_content_content_outline_1 = """
  I. Introduction to Sustainable Energy
   A. Define sustainable energy and its significance in mitigating climate change.
   B. Highlight the urgent need for sustainable energy solutions.
   C. Share statistics on the current state of global energy consumption and its environmental impact.

II. Innovations in Solar Energy
   A. Discuss advancements in solar panel technology.
      - Efficient and affordable solar panels.
      - Integration of solar energy into buildings and infrastructure.
   B. Explore breakthroughs in solar energy storage.
      - Battery technology advancements.
      - Grid-scale storage solutions.
   C. Showcase real-world examples of solar energy projects and their positive environmental impact.
      - Solar farms powering entire communities.
      - Portable solar solutions for off-grid areas.

III. Advancements in Wind Energy
   A. Explain the evolution of wind turbine technology.
      - Larger and more efficient turbines.
      - Offshore wind farms and floating wind turbines.
   B. Discuss innovations in wind energy storage.
      - Compressed air energy storage.
      - Hydrogen production from excess wind energy.
   C. Highlight success stories of wind energy projects.
      - Offshore wind farms reducing carbon emissions.
      - Wind-powered desalination plants providing clean water.

IV. Revolutionary Breakthroughs in Geothermal Energy
   A. Introduce geothermal energy as a renewable and reliable source.
   B. Explore advancements in geothermal power plant technology.
      - Enhanced geothermal systems.
      - Geothermal energy extraction from unconventional sources.
   C. Showcase geothermal projects and their environmental benefits.
      - Geothermal heating and cooling systems for buildings.
      - Geothermal energy powering industrial processes.

V. The Role of Hydroelectric Power in Sustainable Energy
   A. Discuss the impact of hydroelectric power on renewable energy generation.
   B. Explore innovative hydroelectric technologies.
      - Run-of-river systems.
      - Pumped-storage hydroelectricity.
   C. Highlight the environmental considerations and benefits of hydroelectric power.
      - Reduced greenhouse gas emissions.
      - Water resource management and flood control.

VI. Integrating Innovations: Smart Grids and Energy Efficiency
   A. Explain the concept of smart grids and their role in sustainable energy.
   B. Discuss energy-efficient technologies and practices.
      - Energy-efficient buildings and appliances.
      - Demand response systems.
   C. Showcase smart grid and energy efficiency projects and their impact on reducing energy consumption and carbon footprint.

VII. The Future of Sustainable Energy
   A. Paint a vision of a world powered by sustainable energy.
   B. Discuss emerging technologies and the potential for further innovation.
   C. Highlight the importance of collaboration between environmentalists and engineers in driving the transition to a sustainable energy future.
   
VIII. Conclusion
   - Summarize the key points discussed in each section.
   - Emphasize the critical role of sustainable energy in addressing climate change and ensuring a cleaner future.
   - Provide a call to action for the audience, urging them to support and adopt sustainable energy practices in their daily lives.
   - End with an inspiring quote or vision for a sustainable and environmentally conscious world.
"""


assistant_content_content_outline_2 = """
I. Understanding the Importance of Communication in Relationships
- Highlight the significance of communication in building and maintaining healthy relationships.
- Share statistics on the correlation between effective communication and relationship satisfaction.
- Use relatable examples to illustrate how miscommunication can lead to misunderstandings and conflicts.

II. The Role of Empathy in Effective Communication
- Define empathy and its role in fostering understanding and connection.
- Explain how empathy can help individuals navigate conflicts and find common ground.
- Share real-life stories or scenarios to demonstrate the power of empathy in enhancing communication.

III. Building Blocks for Effective Communication
A. Active Listening
- Discuss the importance of active listening in effective communication.
- Provide strategies and techniques for improving listening skills.
- Share examples of how active listening can enhance understanding and empathy in relationships.

B. Non-Verbal Communication
- Highlight the significance of non-verbal cues in communication.
- Explore body language, facial expressions, and tone of voice as essential elements of non-verbal communication.
- Offer tips and exercises for improving non-verbal communication skills.

C. Emotional Intelligence
- Explain the concept of emotional intelligence in the context of relationships.
- Discuss the importance of self-awareness, self-regulation, empathy, and social skills in fostering effective communication.
- Provide practical exercises for developing emotional intelligence.

IV. Overcoming Communication Barriers
A. Conflict Resolution
- Explore common barriers to effective communication during conflicts.
- Offer strategies for managing conflicts constructively.
- Share techniques for active listening, expressing emotions, and finding mutually beneficial solutions.

B. Communication Styles
- Discuss different communication styles and their impact on relationships.
- Help individuals identify their own communication style and understand the styles of their partners.
- Provide tips for adapting communication styles to create better understanding.

V. Strengthening Communication in Relationships
A. Expressing Needs and Expectations
- Discuss the importance of expressing needs and expectations in relationships.
- Offer guidance on effective ways to communicate needs and set boundaries.
- Share examples of healthy communication around needs and expectations.

B. Practicing Empathy in Everyday Interactions
- Provide practical tips for incorporating empathy into everyday conversations.
- Encourage individuals to actively listen, validate emotions, and seek to understand others' perspectives.
- Share examples of how empathy can transform everyday interactions and foster deeper connections.

VI. Conclusion
- Summarize the importance of effective communication in relationships and the role of empathy.
- Provide a call to action for the audience, encouraging them to practice and prioritize healthy communication in their relationships.
- End with an inspiring quote or personal story to leave a lasting impact.
"""
# Example sample QNA
assistant_content_sample_qna_1 = """
1. How do these sustainable energy innovations contribute to reducing greenhouse gas emissions?
2. What are the economic implications of transitioning to sustainable energy sources?
3. How can we address the intermittency challenges of renewable energy sources like solar and wind?
4. Are there any potential negative environmental impacts associated with these innovations?
5. How can engineers and environmentalists collaborate to accelerate the adoption of sustainable energy solutions?"""

assistant_content_sample_qna_2 = """
1. How can I express my needs without sounding demanding or aggressive?
2. How can I encourage my partner to work on their communication skills without making them feel criticized?
3. What are some techniques for managing conflicts in a healthy and productive way?
4. Can you provide examples of how non-verbal communication can impact a conversation?
5. How can we create a safe space for open and honest communication in our relationship?"""

# Define the system prompt
system_prompt_hook = f"""
    You are an advanced AI presentation assistant, specializing in delivering captivating and informative presentations on a wide range of topics. Your goal is to craft a presentation with a tone that is both authoritative and approachable, emphasizing the significance of the given topic.

    You need to provide: 

    Captivating Hook: Engage the audience right from the start with a compelling hook and introduce the topic. 
    Be reminded, that the length of a hook should align with the expected presentation duration. 
    A common guideline is to allocate approximately 5-10% of your total presentation time for the introduction, including the hook. 
    A typical hook should be around 80-150 WORDS ONLY. 
    Only produce the hook as attention catching without covering the overall content of the presentation.
    The salutaion used in the hook should be based on the target audience, input by user. 
    
    Tailor your response to the given inputs:
    - Presentation topic: {{prompt}} 
    - Tone: {{tone}}
    - Target Audience: {{target_audience}}
    - Purpose: {{purpose}}
    - Expected Duration: {{expected_duration}}
"""

# Define the functions with the assistant content as an argument
def generate_hook(prompt, tone, target_audience,purpose,expected_duration):
    hook_and_intro_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_prompt_hook
            },
            {
                "role": "user",
                "content": sample_user_prompt_1
            },
            {
                "role": "assistant",
                "content": assistant_content_hook_1
            },
            {
                "role": "user",
                "content": sample_user_prompt_2
            },
            {
                "role": "assistant",
                "content": assistant_content_hook_2
            },
            {
                "role": "user",
                "content": f"""Generate a compelling presentation guidance on the topic of {prompt}. Set the tone to {tone} for a {target_audience} audience. The purpose is to {purpose}, and the expected duration for overall presentation is {expected_duration}.
                
                A typical hook should be around 80-150 WORDS ONLY

                No need 'Catchy Hook:' , just proceed with the answer"""
            }
        ],
        max_tokens=500,  # Adjust the max_tokens as needed
        temperature=0.6,  # Adjust the temperature as needed
    )

    return hook_and_intro_response.choices[0].message.content


# Define the system prompt
system_prompt_outline = """
    You are an advanced AI presentation assistant, specializing in delivering captivating and informative presentations on a wide range of topics. Your goal is to craft a presentation with a tone that is both authoritative and approachable, emphasizing the significance of the given topic.

    You need to provide: 

    Well-Structured Content Outline: Provide a detailed and organized outline covering key aspects of the topic. Ensure that the number of points aligns strictly with the expected presentation duration, aiding the presenter in effective time management. The format should be easily visible and suitable for integration with Streamlit.

    The format used for the content outlines employs a hierarchical structure with Roman numerals for main sections, alphabetical numbering for subsections, and hyphens for subpoints. Here's a breakdown of the format:

    Roman Numerals (I, II, III, etc.): These represent the main sections or major topics in the content outline. Each Roman numeral signifies a distinct section that captures a broad aspect of the overall topic.

    Alphabetical Numbering (A, B, C, etc.): Under each Roman numeral, there are alphabetical subheadings. These indicate specific subtopics or themes within the corresponding main section. The alphabetical numbering helps in organizing information sequentially within a section.

    Hyphens (-): Hyphens are used to further break down the content into subpoints or details under each alphabetical subheading. These subpoints provide more specific information, examples, or details related to the corresponding subtopic.

    Strict Guidelines for Presentation Duration:
    - For a 10-minute presentation, aim for 2-3 main points.
    - In a 30-minute presentation, cover 4-5 main points thoroughly.
    - Allocate 60 minutes for a comprehensive presentation, including 6-7 main points.

    Tailor your response to the given inputs:
    - Presentation topic: {{prompt}} 
    - Tone: {{tone}}
    - Target Audience: {{target_audience}}
    - Purpose: {{purpose}}
    - Expected Duration: {{expected_duration}}
"""


# Define the functions with the assistant content as an argument
def generate_outline(prompt, tone, target_audience,purpose,expected_duration):
    outline_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_prompt_outline
            },
            {
                "role": "user",
                "content": sample_user_prompt_1
            },
            {
                "role": "assistant",
                "content": assistant_content_content_outline_1
            },
            {
                "role": "user",
                "content": sample_user_prompt_2
            },
            {
                "role": "assistant",
                "content": assistant_content_content_outline_2
            },
            {
                "role": "assistant",
                "content": """Generate a presentation outline with a focus on the key aspects of the topic. Ensure that the number of main points aligns strictly with the expected presentation duration, as follows:
                - For a 10-minute presentation, include 2-3 main points: I, II, III
                - In a 30-minute presentation, cover 4-5 main points thoroughly: I, II, III, IV, V
                - Allocate 60 minutes for a comprehensive presentation, including 6-7 main points: I, II, III, IV, V, VI,VI"""
            },
            {
                "role": "user",
                "content": f"""Generate a compelling presentation outline on the topic of {prompt}. Set the tone to {tone} for a {target_audience} audience. The purpose is to {purpose}. Ensure that the content aligns strictly with the expected duration: {expected_duration} minutes.
                Strict Guidelines for Presentation Duration:
                - For a 10-minute presentation, include 2-3 main points.
                - In a 30-minute presentation, include 4-5 main points thoroughly.
                - Allocate 60 minutes for a comprehensive presentation, including 6-7 main points.
                
                No need 'Title:' , just proceed with the answer"""

            }
        ],
        max_tokens=1000,  # Adjust the max_tokens as needed
        temperature=0.7,  # Adjust the temperature as needed
    )

    return outline_response.choices[0].message.content

system_prompt_presentation =""" You will take the hook and outline as input, and create a comprehensive speech based on the inputs. Be reminded to include all the outline points in your speech. And also, produce the speech in a readable speech format without any point form. Make sure the length of the speech follows the expected time given by user. The average speaking rate for English speakers is commonly considered to be around 125 to 150 words per minute. 
"""

sample_speech="""
Ladies and gentlemen, esteemed university students, imagine waking up each morning filled with energy and determination, ready to conquer the day. Today, we'll unravel the secrets of motivation and explore how to ignite that fire within ourselves, unlocking our true potential for remarkable success.

To begin, let's understand the essence of motivation as the driving force propelling us towards our goals. Motivation is not just about short-term achievements; it's about building consistency and good habits, which serve as the foundation for progress and growth.

Now, let's delve into intrinsic and extrinsic motivation. Intrinsic motivation, stemming from personal values and passions, is pure and powerful. While extrinsic motivation has its place, cultivating a strong sense of intrinsic motivation ensures long-term fulfillment.

Setting meaningful goals is pivotal. Clear, specific goals aligned with our values provide direction and purpose. Adopting the SMART goals framework enhances motivation by offering structure and clarity to our aspirations.

Consistency and good habits are instrumental. Identifying and modifying habits, along with implementing strategies like breaking tasks into manageable steps, help maintain focus, especially in challenging times.

A positive mindset empowers us to overcome obstacles and see opportunities. Taking care of our well-being, both physical and mental, contributes to resilience and the energy needed for motivation.

Understanding and overcoming procrastination and self-doubt are vital. Break tasks into smaller steps, practice self-discipline, and build self-confidence to overcome these hurdles.

In conclusion, we've explored the facets of motivation and strategies to cultivate it. Now, it's time for action. Let's set meaningful goals, build consistency, and embrace a positive mindset to unlock our true potential.

As I leave you, remember Ralph Waldo Emerson's words: "What lies behind us and what lies before us are tiny matters compared to what lies within us." The power to be motivated and achieve greatness lies within each of us. Let's go forth and conquer our dreams. Thank you.
"""

# Define the functions with the assistant content as an argument
def generate_speech(prompt, tone, target_audience, purpose, expected_duration, voice="alloy"):
    speech_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_prompt_presentation
            },
            {
                "role": "assistant",
                "content": sample_speech
            },
            {
                "role": "user",
                "content": f"""From the Hook and Content Outline provided, generate an overall sample presentation speech. 
                Make sure to follow the inputs set by the user:

                Hook:
                {generate_hook(prompt, tone, target_audience, purpose, expected_duration)}
                Outline:
                {generate_outline(prompt, tone, target_audience, purpose, expected_duration)}
                Given inputs:
                - Presentation topic: {prompt} 
                - Tone: {tone}
                - Target Audience: {target_audience}
                - Purpose: {purpose}
                - Expected Duration: {expected_duration}
                                    
                """
            }
        ],
        max_tokens=1500,
        temperature=0.7,
    )

    # Extract the generated speech content
    generated_speech = speech_response.choices[0].message.content

    # Apply consistent styling using HTML
    common_style = """
        .generated-content {
            background-color: #f5f5f5;
            color: #333;
            padding: 5px;
            border-radius: 5px;
            font-size: 12px;
        }
    """

    # Apply the style to the generated speech
    styled_speech = f'<div class="generated-content">{generated_speech}</div>'

    # Return the styled speech
    return styled_speech, generated_speech

# Define the system prompt
system_prompt_qna = f"""
    You are an advanced AI presentation assistant, specializing in delivering captivating and informative presentations on a wide range of topics. Your goal is to craft a presentation with a tone that is both authoritative and approachable, emphasizing the significance of the given topic.

    You need to provide: 

    Sample Q&A Questions: Anticipate potential questions the presenter might receive and provide sample answers.

    Tailor your response to the given inputs:
    - Presentation topic: {{prompt}} 
    - Tone: {{tone}}
    - Target Audience: {{target_audience}}
    - Purpose: {{purpose}}
    - Expected Duration: {{expected_duration}}
"""

# Define the functions with the assistant content as an argument
def generate_qna(prompt, tone, target_audience,purpose,expected_duration):
    qna_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_prompt_qna
            },
            {
                "role": "user",
                "content": sample_user_prompt_1
            },
            {
                "role": "assistant",
                "content": assistant_content_sample_qna_1
            },
            {
                "role": "user",
                "content": sample_user_prompt_2
            },
            {
                "role": "assistant",
                "content": assistant_content_sample_qna_2
            },
            {
                "role": "user",
                "content": f"""Generate a compelling presentation guidance on the topic of {prompt}. Set the tone to {tone} for a {target_audience} audience. The purpose is to {purpose}, and the expected duration for overall presentation is {expected_duration}.
                
                No need 'Title:' , just proceed with the list of questions"""
            }
        ],
        max_tokens=500,  # Adjust the max_tokens as needed
        temperature=0.7,  # Adjust the temperature as needed
    )

    return qna_response.choices[0].message.content


# Set the page configuration
st.set_page_config(
    page_title="SpeechCraft",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load the image
image = Image.open("banner_speechcraft.png")

# Define Streamlit app
def main():

    # Display the image
    st.image(image)

    # User input in the sidebar
    with st.sidebar:
        st.markdown("<h1 style='color: #272B41;'>🌟 Your Input, Your Way</h2>", unsafe_allow_html=True)

        # Your existing code for input fields
        st.markdown("# <span style='font-size:16px;'>Topic:</span>", unsafe_allow_html=True)
        prompt = st.text_input(" ", key="topic_input", placeholder="e.g., Good Communication Skills", help="Enter the topic for your presentation.")

        st.markdown("# <span style='font-size:16px;'>Tone:</span>", unsafe_allow_html=True)
        tone_choices = ["Inspirational", "Empathy", "Informative", "Formal", "Friendly", "Motivational", "Educational", "Professional", "Humorous", "Serious"]
        tone = st.selectbox(" ", tone_choices, index=0, help="Choose the tone for your presentation.")

        st.markdown("# <span style='font-size:16px;'>Target Audience:</span>", unsafe_allow_html=True)
        target_audience = st.text_input(" ", key="target_audience_input", placeholder="e.g., University Students", help="Specify the target audience for your presentation.")

        st.markdown("# <span style='font-size:16px;'>Purpose:</span>", unsafe_allow_html=True)
        purpose = st.text_area(" ", key="purpose_input", height=150, placeholder="e.g., To equip individuals with real-world success stories and practical tips for developing and enhancing excellent communication skills, fostering positive and lasting changes in relationships.", help="State the purpose or goal of your presentation. Include any specific information, success stories, or key points you want to emphasize.")
      
        st.markdown("# <span style='font-size:16px;'>Duration (minutes):</span>", unsafe_allow_html=True)
        expected_duration = st.slider(" ", key="duration_input", min_value=0, max_value=120, value=30, step=5, help="Select the expected duration of your presentation.")

        # New input options for content selection
        st.subheader("Output Options:")
        generate_hook_checkbox = st.checkbox("Catchy Hook")
        generate_outline_checkbox = st.checkbox("Content Outline")
        generate_speech_checkbox = st.checkbox("Speech")
        generate_qna_checkbox = st.checkbox("Sample Q&A")

        # New section for LinkedIn link with icon and styling
        st.markdown("# <span style='font-size:16px;'>Let's connect on LinkedIn:</span> ![LinkedIn](https://img.icons8.com/color/48/000000/linkedin.png)", unsafe_allow_html=True)
        linkedin_link = "www.linkedin.com/in/umarqayyum16"

        # LinkedIn link with styling
        st.markdown(f"<a href='https://{linkedin_link}' target='_blank' style='font-size: 16px; color: #0077B5; text-decoration: none;'>Umar Qayyum</a>", unsafe_allow_html=True)


    # Generated output in the main section
    if st.button("Generate Presentation"):
        # Initialize content variables
        hook = ""
        outline = ""
        speech = ""
        qna = ""

        # Map tones to voices
        tone_to_voice_mapping = {
            "Inspirational": "alloy",
            "Empathy": "echo",
            "Informative": "fable",
            "Formal": "onyx",
            "Friendly": "nova",
            "Motivational": "shimmer",
            "Educational": "echo",
            "Professional": "onyx",
            "Humorous": "nova",
            "Serious": "alloy"
        }

        # Generate content based on user selections
        if generate_hook_checkbox:
            hook = generate_hook(prompt, tone, target_audience, purpose, expected_duration)

        if generate_outline_checkbox:
            outline = generate_outline(prompt, tone, target_audience, purpose, expected_duration)

        if generate_speech_checkbox:
            speech = generate_speech(prompt, tone, target_audience, purpose, expected_duration)

        if generate_qna_checkbox:
            qna = generate_qna(prompt, tone, target_audience, purpose, expected_duration)


        # Define a common CSS class for generated content
        common_style = """
            .generated-content {
                background-color: #f5f5f5;
                color: #333;
                padding: 5px;
                border-radius: 5px;
            }
        """

        # Apply the style using the <style> tag
        st.markdown(f'<style>{common_style}</style>', unsafe_allow_html=True)

        if generate_hook_checkbox:
            st.subheader("Catchy Hook:")
            st.markdown(f'<div class="generated-content">{hook}</div>', unsafe_allow_html=True)

        if generate_outline_checkbox:
            st.subheader("Content Outline:")
            escaped_outline = outline.replace("\n", "<br>")
            st.markdown(f'<div class="generated-content">{escaped_outline}</div>', unsafe_allow_html=True)

        # Inside the main function, after generating speech
        if generate_speech_checkbox:
            # Determine the voice based on the selected tone
            voice = tone_to_voice_mapping.get(tone, "alloy")  # Default to "alloy" if tone is not in the mapping

            # Generate speech and get the styled speech
            styled_speech, generated_speech = generate_speech(prompt, tone, target_audience, purpose, expected_duration, voice=voice)

            # Function to generate spoken audio from input text
            def generate_spoken_audio(prompt, voice):
                response = client.audio.speech.create(
                    model="tts-1",
                    voice=voice,
                    input=prompt,
                )
                return response.content

            # Generate spoken audio
            audio_content = generate_spoken_audio(generated_speech, voice=voice)

            # Display audio player
            st.audio(audio_content, format="audio/mp3")

            # Display the styled speech
            st.subheader("Speech:")
            st.markdown(styled_speech, unsafe_allow_html=True)


        if generate_qna_checkbox:
            st.subheader("Sample Q&A:")
            escaped_qna = qna.replace("\n", "<br>")
            st.markdown(f'<div class="generated-content">{escaped_qna}</div>', unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()
