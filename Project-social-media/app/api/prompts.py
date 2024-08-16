from langchain.prompts import PromptTemplate


llm_prompt_template = PromptTemplate(
    input_variables=["social", "topic", "details"],
    template="""
    Write a {social} media post about {topic}.
    Do not include sentences like "Here's a possible LinkedIn media post:" or "Let me know if you'd like me to make any changes!".

    The post should:
    - Start with an enthusiastic and professional tone.
    - Express gratitude and excitement for the new role.
    - Maximum 2 short paragraphs
    - Reflect on the journey and career growth leading to this point.
    - Highlight key aspects of the new role and how it aligns with your career goals.
    - Include a forward-looking statement about your aspirations in this new position.
    - Include hashtags at the end of the text.
    Details to include:
    {details}
    """
    )


img_gen_template = """
Create a vibrant and eye-catching image for a social media post about {topic}. The image should:
- Exclude text.
- Reflect the essence of {topic} creatively.
- Include relevant visual elements for {topic}.
- Be suitable for {social} media, considering typical dimensions and aesthetics.
- Incorporate any details or themes mentioned: {details}.

For example, for "summer vacation," show sunny beaches and happy people. For "winter sports," depict snowy mountains and skiers.

Be imaginative and ensure the image matches the post's mood and message.
"""