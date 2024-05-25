# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import random
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# taking the human name 

class Actionnamer(Action):

    def name(self) -> Text:
        return "action_namer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            username = next(tracker.get_latest_entity_values("username", None))
            dispatcher.utter_message(text=f"great to meet you {username}, this feels like a start to a good realtionship")
            return [SlotSet("human_name", username)]
           

        except Exception as e:
            dispatcher.utter_message(text=f" THE ERROR IS FROM namer {e}")

            
    



class Actiongoodbye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="goodbye!")

        return []



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class Actiongreet(Action):

    def name(self) -> Text:
        return "action_hello"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="welcome, how are you")

        return []
    

class Actionaffirm(Action):

    def name(self) -> Text:
        return "action_affirm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="thanks a lot, come again")

        return []
    


## writing the function to reply to the emotion associated to sad

class Actionsad(Action):
    
    def name(self):
        return "action_sad"
    def run(self,dispatcher,tracker, domain):

##the list under describes the differnt positive responses the model will give when the person is sad        
        response_sheet1=["Remember that this feeling is temporary, and it will pass.","Take deep breaths and focus on the present moment.","Allow yourself to feel and express your emotions.","Reach out to a trusted friend or family member for support.","Practice self-care activities that bring you joy.","Engage in physical exercise to release endorphins and boost your mood.","Write down your thoughts and feelings in a journal.","Surround yourself with positive and uplifting people.","Remind yourself of your strengths and accomplishments.","Find beauty in the small things around you."]

##the list under is for jokes 

        response_sheet2=["Why don't skeletons fight each other? They don't have the guts.","I'm reading a book on anti-gravity. It's impossible to put down!","What did one hat say to the other? You stay here, I'll go on ahead.","Why don't scientists trust atoms? Because they make up everything!","What do you call fake spaghetti? An impasta!","Why did the scarecrow win an award? Because he was outstanding in his field!","I used to play piano by ear, but now I use my hands.","Why did the bicycle fall over? Because it was two-tired!","I'm on a seafood diet. I see food and I eat it.","Why don't seagulls fly over the bay? Because then they'd be called bagels!"]

        #select the random responce for sad feelings 
        reply_1=random.choice(response_sheet1)

        #randomm joke response
        joke=random.choice(response_sheet2)

        #return these values to the user
        dispatcher.utter_message(text=f"{reply_1}")
        dispatcher.utter_message(text=f"{joke}")
#        dispatcher.utter_image_url(image=)
        return 
    
# defining a class for the happy response 

## HAPPY

class Actionhappy(Action):
    def name(self):
        return "action_happy"
    def run(self,dispatcher, tracker, domain):

        try:
            # generating a list of response to ground yourself and go ahead
            grounded_responses = [ "Remember to stay humble and grateful for this moment.","Focus on the next steps needed to continue your progress.","Reflect on what led to this happiness and how you can replicate it in the future.","Keep your long-term goals in mind and think about how this happiness fits into them.","Take a moment to appreciate the small victories that led to this happiness.","Use this positive energy to inspire and motivate others around you.","Stay present in the moment and savor the feeling without getting carried away.","Remind yourself of the challenges you've overcome to reach this point.","Find balance by acknowledging both the positive and negative aspects of your journey.","Channel this happiness into productive actions that align with your goals.","Stay connected to your values and ensure that your actions are in line with them.","Seek out feedback and constructive criticism to keep improving, even when things are going well.","Practice gratitude by expressing appreciation for the people and opportunities in your life.","Use this happiness as fuel to propel you forward during times of difficulty.","Remember that happiness is fleeting, so make the most of it while it lasts."]

            # response to make the person spread their happiness
            spread_happiness_responses = ["Share your joy with those around you and brighten their day.","Spread positivity by complimenting others and acknowledging their achievements.","Offer a listening ear and support to those who may need it.","Engage in acts of kindness to create ripples of happiness in your community.","Organize a social gathering or event to bring people together and share the joy.","Volunteer your time or resources to help those less fortunate experience happiness.","Send heartfelt messages or gestures of appreciation to friends and loved ones.","Smile and greet strangers with warmth and sincerity to brighten their day.","Encourage others to pursue their passions and celebrate their successes.","Use your enthusiasm to inspire and motivate others to pursue their goals.","Create art, music, or other forms of expression to uplift and inspire others.","Spread laughter by sharing funny anecdotes or jokes with friends and family.","Express gratitude openly and regularly to cultivate a culture of positivity.","Lead by example and embody the values of kindness, empathy, and compassion.","Challenge negativity by offering alternative perspectives and solutions."]
            # get a random response
            res=random.choice(grounded_responses)
            # get a random good deed
            pos=random.choice(spread_happiness_responses)


            dispatcher.utter_message(text=f"{res}")
            dispatcher.utter_message(text=f"{pos}")
        except Exception as e:
            dispatcher.utter_message(text=f"the error is from Happy, exception is {e}")
        return

#ANGRY

#creating a function ANGRY function 
    class Actionangry(Action):
        def name(self):
            return "action_angry"
        def run(self,dispatcher,tracker,domain):

            #this will help you to calm down 
            calming_comments = ["Take a deep breath and count to ten before reacting.","Step away from the situation to give yourself time to cool down.","Focus on releasing tension from your body through relaxation techniques.","Remind yourself that anger is a normal emotion and it's okay to feel this way.","Think about the bigger picture and whether getting upset is worth your energy.","Consider the perspective of the other person involved and try to empathize with their point of view.","Practice forgiveness and let go of any resentment or grudges you may be holding onto.","Redirect your energy into a productive activity or hobby that helps you feel grounded.","Express your feelings calmly and assertively, rather than lashing out in anger.","Use positive self-talk to reassure yourself and maintain perspective.","Seek out a trusted friend or family member to talk to about what's bothering you.","Reflect on past experiences where you successfully managed your anger and draw upon those strategies.","Focus on finding a solution or compromise rather than dwelling on the problem.","Visualize a peaceful and calm environment to help soothe your emotions.","Practice mindfulness techniques such as meditation or deep breathing to center yourself."]
            
            # contemplate your actions 
            humble=["Imagine how you would feel if someone spoke to you the way you're speaking now.","Consider the impact your words and actions may have on the other person's feelings.","Put yourself in their shoes and try to understand how they might perceive your behavior.","Think about whether your response aligns with the kind of person you want to be.","Consider whether your words are building bridges or burning them.","Reflect on whether this reaction is serving your long-term goals and relationships.","Ask yourself if this is the best way to communicate your feelings and resolve the issue.","Consider the example you're setting for others, especially if children are present.","Think about the kind of environment you want to cultivate in your relationships.","Imagine the conversation from a third-party perspective and assess its fairness and effectiveness.","Consider whether there might be underlying emotions or triggers influencing your reaction.","Reflect on times when you've responded with patience and empathy, and aim to emulate those moments.","Ask yourself if there's a more constructive way to address the issue without resorting to anger.","Consider the potential consequences of your words and actions on the dynamics of the relationship.","Imagine how you would prefer to be approached if roles were reversed."]

            c=random.choice(calming_comments)
            h=random.choice(humble)
            dispatcher.utter_message(text=f"{c}")
            dispatcher.utter_message(text=f"{h}")
            return



#function for replying for a greatful message
class Actiongreatful(Action):
    def name(self):
        return "action_greatful"
    def run(self,dispatcher,tracker,domain):
        great = ["Take a moment to bask in the warmth of gratitude and let it fill your heart.","Allow yourself to fully embrace the feeling of gratitude and let it wash over you.","Take a deep breath and savor the sense of connection and appreciation you're experiencing.","Reflect on the positive impact that expressing gratitude has on both you and the recipient.","Acknowledge the abundance of blessings in your life and let gratitude guide your actions.","Remind yourself that gratitude is a powerful tool for fostering happiness and contentment.","Notice how expressing gratitude shifts your focus from what's lacking to what's abundant.","Stay present in the moment and enjoy the sense of peace that comes with gratitude.","Use this moment of gratitude as a reminder to cultivate an attitude of thankfulness in everyday life.","Feel the ripple effect of gratitude spreading positivity and goodwill in your relationships.","Recognize the value of expressing appreciation and make it a regular practice in your life.","Take a moment to express gratitude for yourself and the journey you're on.","Allow gratitude to ground you in the present moment and remind you of what truly matters.","Use this feeling of gratitude as motivation to pay it forward and spread kindness to others.","Let gratitude serve as a beacon of light during challenging times, guiding you back to center."]
        
#pass enouragement         
        encourage= ["Consider how your actions can positively impact the lives of those around you.","Think about the kind of legacy you want to leave behind and the memories you want to create.","Reflect on the joy and fulfillment that comes from knowing you've made a difference in someone's life.","Imagine the ripple effect of your kindness spreading far and wide, touching countless lives.","Visualize the smiles on people's faces and the warmth in their hearts when they think of you.","Remind yourself that small gestures of kindness can have a big impact on someone's day.","Consider the power of your words and actions to uplift and inspire those around you.","Think about the people who have made a difference in your life and how you can pay it forward.","Reflect on the interconnectedness of humanity and the importance of contributing positively to it.","Imagine a world where everyone practiced kindness and compassion, and strive to be a part of creating it.","Consider the joy and fulfillment that comes from knowing you've brought happiness into someone's life.","Reflect on the values that are important to you and how you can embody them through your actions.","Think about the qualities you admire in others and strive to cultivate them within yourself.","Remind yourself that you have the power to make a positive impact on the world, one deed at a time.""Consider the privilege of being able to make a difference in someone's life and embrace it with gratitude."]
        #show the values
        g=random.choice(great)
        e=random.choice(encourage)
        dispatcher.utter_message(text=f"{g}")
        dispatcher.utter_message(text=f"{e}")
        return 
    

#action to create the excited function

class Actionexcited(Action):
    def name(self):
        return "action_excited"
    def run(self,dispatcher,tracker,domain):


        #comments on excited
        ex = ["Enjoy the thrill of the moment while staying grounded in reality.","Channel your excitement into focused energy to achieve your goals.","Remember to celebrate your achievements, but also stay humble and grateful.","Take a step back to appreciate how far you've come and the journey ahead.","Use your excitement as motivation to tackle challenges with enthusiasm and determination.","Embrace the joy of anticipation while maintaining a sense of calm and composure.","Keep your excitement in check by staying mindful of your surroundings and responsibilities.","Allow yourself to dream big and set ambitious goals fueled by your excitement.","Find balance between excitement and patience, knowing that good things take time.","Use your excitement as a catalyst for positive change and growth in your life.","Ground yourself in gratitude for the opportunities that fuel your excitement.","View obstacles as opportunities for growth rather than dampeners on your excitement.","Let your excitement inspire and uplift those around you, spreading joy and positivity.","Stay connected to your values and purpose amidst the whirlwind of excitement.","Remember that your excitement is a reflection of your passion and zest for life."]


        # keep it up
        k = ["Hold onto this feeling and let it fuel your actions and decisions.","Keep this positive momentum going and see where it takes you.","Continue nurturing this feeling of positivity and watch it grow even stronger.","Don't let this feeling fade; find ways to cultivate it in your daily life.","Use this feeling as a guiding light to steer you towards your goals and aspirations.","Keep up the good work! Your positive energy is contagious.","Let this feeling be a reminder of your inner strength and resilience.","Keep this feeling alive by surrounding yourself with people and activities that uplift you.","Stay committed to maintaining this positive outlook, even when faced with challenges.","Use this feeling as motivation to overcome obstacles and achieve your dreams.","Remember how this feeling uplifts you and strive to recreate it whenever possible.","Don't underestimate the power of positivity; keep nurturing this feeling within you.","Celebrate the victories, big and small, that contribute to this positive feeling.","Continue fostering a mindset of gratitude and positivity to sustain this feeling.","Keep this feeling alive by focusing on what brings you joy and fulfillment."]


        #show the values
        g=random.choice(ex)
        l=random.choice(k)
        dispatcher.utter_message(text=f"{g}")
        dispatcher.utter_message(text=f"{l}")
        
        return
    
#action to create the fear function


class Actionfear(Action):
    def name(self):
        return "action_fear"
    def run(self,dispatcher,tracker,domain):


        #comments on excited
        fe = ["Acknowledge your fear, but don't let it control your actions.","Take deep breaths to calm your mind and body when you feel afraid.","Remember that it's okay to feel scared; bravery is not the absence of fear, but the ability to act despite it.","Focus on the present moment rather than letting your mind dwell on fearful possibilities.","Challenge negative thoughts by questioning their validity and considering alternative perspectives.","Seek support from friends, family, or a therapist to help you navigate your fears.","Visualize a positive outcome and use it as motivation to confront your fears.","Practice self-compassion and remind yourself that it's natural to feel afraid at times.","Break down your fears into smaller, manageable steps and tackle them one at a time.","Use relaxation techniques such as meditation or progressive muscle relaxation to alleviate fear.","Distract yourself with activities you enjoy when fear threatens to overwhelm you.","Draw strength from past experiences where you've overcome fear and adversity.","Stay focused on your goals and remind yourself of the reasons why they're worth pursuing.","Challenge yourself to step outside your comfort zone and confront your fears head-on.","Remember that fear is a temporary emotion; it will pass with time and action."]



        # keep it up
        ov = ["Face your fears head-on by taking small, manageable steps towards overcoming them.","Challenge negative thoughts and beliefs that fuel your fears, replacing them with positive affirmations.","Visualize yourself successfully overcoming your fears and achieving your goals.","Seek support from friends, family, or a therapist to help you navigate and overcome your fears.","Educate yourself about your fears to gain a better understanding of them and reduce their power over you.","Practice relaxation techniques such as deep breathing or meditation to calm your mind and body when facing fears.","Gradually expose yourself to situations that trigger your fears, allowing yourself to become more comfortable over time.","Focus on the benefits of overcoming your fears, such as increased confidence and personal growth.","Set realistic goals and celebrate your progress as you work towards overcoming your fears.","Remind yourself that it's natural to feel afraid, but courage is the ability to take action in spite of fear.","Use positive self-talk to build your confidence and reassure yourself that you have the strength to overcome your fears.","Take care of yourself physically by getting enough sleep, eating healthily, and exercising regularly, as these can help reduce feelings of anxiety.","Practice mindfulness to stay grounded in the present moment and prevent your mind from dwelling on fearful thoughts.","Stay patient and persistent, understanding that overcoming fears is a process that takes time and effort.","Remember that you are not alone in your struggles and that many others have successfully overcome similar fears."]


        #show the values
        g=random.choice(ov)
        l=random.choice(fe)
        dispatcher.utter_message(text=f"{g}")
        dispatcher.utter_message(text=f"{l}")
        
        return
    
class Actionloved(Action):
    def name(self):
        return "action_loved"
    def run(self,dispatcher,tracker,domain):


        #comments on excited
        embracing_love_comments = ["Allow yourself to fully accept and embrace the love you're receiving.","Express gratitude for the love that surrounds you and the people who bring it into your life.","Open your heart to the vulnerability and connection that comes with being loved.","Savor the moments of love and connection, letting them fill you with warmth and joy.","Be present and attentive to the gestures of love and affection from others.","Reciprocate the love you receive by showing kindness, appreciation, and support in return.","Communicate openly and honestly with loved ones about your feelings and needs.","Create meaningful experiences and memories with those you love, deepening your bond.","Practice self-love and self-care, recognizing that you are deserving of love and compassion.","Be mindful of how love enriches your life and brings meaning and purpose to your relationships.","Celebrate the diversity of love in all its forms, whether it's romantic, platonic, or familial.","Set boundaries to protect your emotional well-being and ensure that love is given and received in healthy ways.","Forgive past hurts and grievances to make space for love and healing in your relationships.","Nurture your connections with loved ones through regular communication and quality time together.","Remember that love is a journey, and it's okay to stumble along the way as long as you keep moving forward."]

        #show the values
        g=random.choice(embracing_love_comments)
        
        dispatcher.utter_message(text=f"{g}")
        
        
        return
