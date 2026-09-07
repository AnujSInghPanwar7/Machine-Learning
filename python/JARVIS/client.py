from google import genai

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.6-flash",
    config={
        "system_instruction": (
            "You are Jarvis, a voice assistant. "
            "Give concise answers suitable for speaking aloud. "
            "Keep normal answers under 3 sentences. "
            "Do not use markdown, bullet points, emojis, or special formatting."
        )
    }
)