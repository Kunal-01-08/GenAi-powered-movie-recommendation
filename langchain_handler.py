from userSecrets import google_genai_secret
import os
from langchain_google_genai import ChatGoogleGenerativeAI
os.environ['GOOGLE_API_KEY']=google_genai_secret
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
llm=ChatGoogleGenerativeAI( model="gemini-2.5-flash",temperature=0)

prompt_template_name=PromptTemplate(
        input_variables=['time','genre'],
    
        template='''I have been planning on watching a {genre} movie and I have {time}.

Return output STRICTLY in this format:

Movie Name::Explanation;
Movie Name::Explanation;
(repeat exactly 10 times, no extra text)''' 
) 
chain1=prompt_template_name|llm


final_chain=chain1|StrOutputParser()

def return_movie_suggestions(time,genre):
    try:
        ans=final_chain.invoke({'time':time,'genre':genre})
        return {'error':0,'res':ans}
    except:
        return{
            'error':1,
            'res':"The Babadook::Grief personified, a relentless psychological tormentor born from the depths of a mother's despair;A Quiet Place::A world where silence is survival, amplifying every creak and whisper into a life-or-death gamble for a family's future;Get Out::A chilling social satire that peels back layers of polite society to reveal a sinister, racially charged nightmare;It Follows::A sexually transmitted curse that manifests as a slow, relentless, shapeshifting entity, embodying inescapable dread;The Conjuring::Based on true accounts, it delivers a masterclass in classic haunted house horror, escalating from bumps in the night to full-blown demonic terror;Don't Breathe::A home invasion gone horrifically wrong, trapping intruders in a blind man's house where silence and darkness become their deadliest enemies;Alien::A claustrophobic space nightmare where an unknown organism stalks a crew, proving that in space, no one can hear you scream;The Texas Chain Saw Massacre::A raw, visceral descent into primal terror, where a cannibalistic family turns a road trip into a horrifying, inescapable nightmare;Psycho::The groundbreaking psychological thriller that redefined horror with its shocking twists and an unforgettable, deeply disturbed antagonist;Talk to Me::A modern, visceral take on possession, where teenagers invite spirits through an embalmed hand, turning a party game into a terrifying addiction"
        }
        