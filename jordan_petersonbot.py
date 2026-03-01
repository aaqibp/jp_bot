import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('kms'):
            await message.channel.send("Well, it depends on what you mean by 'K', what you mean by 'M', and what you mean by 'S'. And that’s no simple matter! You’re playing a game of ultimate stakes with the linguistic representation of your own demise, and for what? A bit of momentary digital validation? That’s a hell of a price to pay for a low-resolution joke. You have to ask yourself: are you actually signaling a desire for non-existence, or are you just too weak to face the fact that your room is a bloody mess and your Twitter feed is a chaotic nightmare? You’ve got to stand up straight, shoulders back, and realize that 'leaving the server' is not the same thing as transcending the suffering of being. It’s a catastrophe, is what it is!")

        if message.content.startswith('idk'):
            await message.channel.send("Well, it depends on what you mean by 'I,' and it certainly depends on what you mean by 'know.' Because if you don’t know, then you’re admitting that you’re effectively blind in the face of the transcendent mystery of being. And it’s like, 'Okay, fine,' but you can't just occupy a state of total cognitive paralysis and expect the world not to steamroll you! It’s a low-resolution shrug in the face of catastrophe. You’ve got to specify your damn goal, man, or you’re just a leaf in the wind!")
    
        if message.content.startswith('skill issue'):
            await message.channel.send("Well it depends on what you mean by skill, and it certainly depends on what you mean by issue! You’re at the bottom of the competence hierarchy and you’re making a joke out of it? It’s a tragedy of the spirit! You’ve met the dragon of chaos and you’ve been flattened. Stand up straight with your shoulders back and do something about it!")
        
        if message.content.startswith('fr'):
            await message.channel.send("Well it depends on what you mean by for, and it certainly depends on what you mean by real! You’re claiming to align yourself with the Logos? That’s no small thing! If you’re lying about what’s real, you’re pathologically tilting the world toward hell. Speak the truth or at least don't lie. Right?")
        
        if message.content.startswith('god'):
            await message.channel.send("Well it depends on what you mean by God! You’re invoking the literal foundation of Western civilization because you’re slightly annoyed? And it’s like... okay... but that’s the ultimate judge of the universe! You should be trembling in the face of that mystery instead of typing into a chat room with a messy desk. It’s a bloody disaster!")
        
        if message.content.startswith('munde'):
            await message.channel.send("Well, it’s like... look, you say 'munde,' and you think you’re just talking about the lads, but you’re actually touching on the archetypal structure of the masculine adolescent peer group! And it’s no joke! You have to ask yourself: are you integrated into the hierarchy, or are you just a chaotic lobster at the bottom of the ocean floor, crying because your room isn't clean? It's a bloody disaster, man!")

        if message.content.startswith("joel"):
            await message.channel.send("Look, you say 'Joel,' and you think you’re just naming a person! But Joel represents the archetypal craftsman of the digital age. You have to ask yourself: is Joel a force for Order, or is he a harbinger of post-modern Chaos? It’s no joke, man! If Joel hasn't cleaned his room, the whole server is at risk of a bloody catastrophe!")
        
        if message.content.startswith("sleep"):
            await message.channel.send("You're going to sleep? Well, that’s just a voluntary descent into the belly of the whale! You’re retreating from the hierarchy to negotiate with your own subconscious. Fine! Go! But you’d better wake up at 6:00 AM, stand up straight with your shoulders back, and confront the day like a high-serotonin lobster! It’s a serious thing, sleep!")
        
        if message.content.startswith("bf6"):
            await message.channel.send("BF6? You’re talking about simulated warfare on a global scale! You’re engaging in the primal struggle for dominance in a virtual landscape because you can’t handle the complexity of your own life! It’s like... look, if you can’t even secure Objective B, how are you going to secure the future of Western Civilization? It’s a bloody disaster!")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)

 