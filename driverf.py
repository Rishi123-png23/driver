
import requests
import streamlit as st
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu


#  find more emojis here : https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title = "DRIVER SAFETY SYSTEM/RISHI_JRK" , page_icon ="https://vjit.ac.in/campus-life/clubs/#",layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return r.json()

hide_st_style = """
                <style>
                #MainMenu { visibility : hidden;}
                footer { visibility : hidden;}
                header { visibility : hidden;}
                </style>
                """
st.markdown(hide_st_style , unsafe_allow_html = True)
                

# use local css
def local_css(file_name):
    with open(file_name) as f :
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
#animations

img_p1 = Image.open("pics/p1.jpg")
img_p2 = Image.open("pics/p2.jpg")
img_p3 = Image.open("pics/p3.jpg")
img_p4 = Image.open("pics/p4.jpg")
img_p5 = Image.open("pics/p5.jpg")
img_p6 = Image.open("pics/p6.jpg")
img_p7 = Image.open("pics/p7.jpg")
img_p8 = Image.open("pics/p8.jpg")
img_p9 = Image.open("pics/p9.jpg")
img_p10 = Image.open("pics/p10.jpg")
img_p11 = Image.open("pics/p11.jpg")
img_p12 = Image.open("pics/p12.jpg")
img_p13 = Image.open("pics/p13.jpg")
img_p14 = Image.open("pics/p14.jpg")
img_p15 = Image.open("pics/p15.jpg")
img_p16 = Image.open("pics/p16.jpg")
img_p17 = Image.open("pics/p17.jpg")
img_p18 = Image.open("pics/p18.jpg")
img_p19 = Image.open("pics/p19.jpg")
img_p20 = Image.open("pics/p20.jpg")
#st.image(img_logo,width = 220, use_column_width = 70 )

                                  

#horizontal menu
selected = option_menu(
        menu_title ="",
        options =["home","Clear-Value-Proposition","Target-Audeince","Market-Stratagy","Revenue","Contact"],
        icons = ["house","globe","book","tv","book","pin-map","person-fill"],
        menu_icon = "cast",
        default_index = 0,
        orientation = "horizontal")
        
if selected == "home":
              
              with st.container():
                    #st.subheader("DRIVER SAFETY SYSTEM")
                    st.title("DRIVER SAFETY SYSTEM")
                    st.image(img_p1, caption = "VJIT")
              with st.container():
                    st.write("-----")
                    #left_column,right_column = st.columns(2)
                    st.header("Problem statement")
                    st.write("###")
                    st.write("""
- Various studies have suggested that around 20% of all road accidents are fatigue-related, up to 50% on certain roads,driver fatigue is a significant factor in a large number of vehicle accidents.

- Recent statistics estimate that annually 1,200 deaths and 76,000 injuries can be attributed to fatigue related crashes.

- The development of technologies for detecting or preventing drowsiness at the wheel is a major challenge in the field of accident avoidance systems.

- Because of the hazard that drowsiness presents on the road,methods need to be developed for counteracting its affects. related,up to 50% on certain roads.

- Driver fatigue is a significant factor in a large number of vehicle accidents.

- Recent statistics estimate that annually 1,200 deaths and 76,000 injuries can be attributed to fatigue related crashes.

- The development of technologies for detecting or preventing drowsiness at the wheel is a major challenge in the field of accident avoidance systems.

- Because of the hazard that drowsiness presents on the road, methods need to be developed for counteracting its effect.

""")
        
                
                      
              with st.container():
                    st.write("-------")
                    st.header("Previous Data Analysis")
                    st.image(img_p2,width = 550, use_column_width = 390)
                    st.write("""
- Driver’s inattention might be the result of a lack of alertness when driving due to driver drowsiness and distraction.

- Driver distraction occurs when an event draws a person’s attention away from the driving.

- Unlike driver distraction, driver drowsiness involves no triggering event but, instead,is characterized by a progressive withdrawal of attention from the road and traffic demands.

- Both driver drowsiness and distraction, however, might have the same effects, that is decreased driving performance, longer reaction time,and an increased risk of  crash.

- Fatigue and drowsiness have caused countless accidents worldwide.
- 1 Drowsiness and fatigue in drivers have been recognized as an important factor causing severe casualties in traffic accidents.
- 2-5 Statistics revealed that 20 to 40 percent of traffic accidents in Iran are due to drivers' fatigue.
- 6 The impact of fatigue and drowsiness on drivers could be more severe consequences due to the lack of avoidance or corrective action, poor speed control,and slower reaction time.7,8 The U.S.
- National Highway Traffic Safety Administration (NHTSA) estimated that 56,000 drowsiness accidents occur annually, in 1,550 fatalities and 40,000 injuries.9
-In Australia, fatigue accounted for 15% of heavy vehicle fatal crashes and 10% of total injury crashes,incurring more than $250 million costs.10

""")
              with st.container():
                    st.write("-----")
                    #left_column,right_column = st.columns(2)
                    #st.header("Problem statement")
                    st.image(img_p3,width = 650, use_column_width = 550)
                    st.write("""
- Drowsiness detection is one of those common problem needed to be solved to prevent road accidents.

- In recent time's automobile fatigue connected crashes have very enlarged.

- In this paper, we propose improved mobile-Net transfer learning approach to overcome the limitations of existing approaches and reinforcementon big data analytics.

- The Mobile-Net model is a CNN architecture that was constructed to be implemented on an embedded board.

- However, there are constraints of such architecture for the hardware deployment, which is the limited memory of micro-controller units.

- This paper proposes an enhanced version of Mobile-Net that verify the condition to be implemented on an embedded board while improved the accuracy.

- Mobile-Net has fewer number of layers, improved accuracy while depreciating the overall size of the model and lower average time compared to the Mobile-Net-VI.
                  
""")
                    
                    

if selected == "Clear-Value-Proposition":
            with st.container():
                      st.write("-------")
                      st.title("DETECTION SYSTEM")
                      st.subheader("What is driver safety system ?")
                      st.write("---")
                      st.image(img_p4)
                      st.write("""
- we propose improved mobile-Net transfer learning approach to overcome the limitations of existing approaches and reinforcement on big data analytics.
- The Mobile-Net model is a CNN architecture that was constructed to be implemented on an embedded board.However, there are constraints of such architecture for the hardware deployment,
- which is the limited memory of micro-controller units.This paper proposes an enhanced version of Mobile-Net that verify the condition to be implemented on an embedded board while improved the accuracy.
- Mobile-Net has fewer number of layers,improved accuracy while depreciating the overall size of the model and lower average time compared to the Mobile-Net-VI.
- The driver drowsiness detection is based on an algorithm,which begins recording the driver’s steering behavior the moment the trip begins.
- It then recognizes changes over the course of long trips, and thus also the driver’s level of fatigue.
- Typical signs of waning concentration are phases during which the driver is barely steering, combined with slight,
- yet quick and abrupt steering movements to keep the car on track.
- Based on the frequency of these movements and other parameters,among them the length of a trip, use of turn signals, and the time of day,the function calculates the driver’s level of fatigue.
- If that level exceeds a certain value,an icon such as a coffee cup flashes on the instrument panel to warn drivers that they need a rest.
""")
                      st.image(img_p5)
                      st.write("""
- A non-invasive system to localize the eyes and monitor fatigue was developed.
- Information about the eyes position is obtained through self-developed image processing algorithm.
- During the monitoring, the system is able to decide if the eyes are opened or closed.
- When the eyes have been closed for 10-15 frames  a warning signal is issued.
- In addition, during monitoring,the system is able to automatically detect any eye localizing error that might have occurred.
- In case of this type of error, the system is able to recover and properly localize the eyes
""")
                      st.image(img_p6)
                      st.write("""
• Driver drowsiness detection is a car safety technology which helps to save the life of the driver by preventing accidents when the driver is getting drowsy.

 • The main objective is to first design a system to detect driver’s drowsiness by continuously monitoring retina of the eye. 

• The system works in spite of driver wearing spectacles and in various lighting conditions.

 • To alert the driver on the detection of drowsiness by using buzzer or alarm. 

• Speed of the vehicle can be reduced. 

• Traffic management can be maintained by reducing the accidents.


""")


if selected == "Target-Audeince":
    with st.container():
        st.title("Target Audience")
        st.image(img_p8)
        st.subheader("Fleet mangers and logistics compaines:")
        st.write("These organizations would benefit from implementing driver drowsiness detection systems as a means of reducing the risk of accidents caused by drowsy driving among their drivers.")
        st.subheader("Truck drivers:")
        st.write("""
Drivers who operate heavy-duty vehicles,especially those who are required to drive long distances or work irregular hours, could benefit from using a driver drowsiness detection system to help them stay alert and focused on the road.
                        """)
        st.subheader("commuters and travelers:")
        st.write ("""
Individuals who commute long distances or regularly take road trips could benefit from using a drowsiness detection system to monitor their own fatigue levels and prevent accidents.

""")
        st.subheader(" Automobile manufacturers:")
        st.write("""
Car manufacturers may be interested in incorporating drowsiness detection systems into their vehicles as a safety feature.
                    """)
        st.subheader("Government agencies and safety organizations :")
        st.write ("""
Organizations such as the National Highway Traffic Safety Administration (NHTSA) and the World Health Organization (WHO) could promote the adoption of driver drowsiness detection systems as part of their efforts to reduce the number of accidents caused by drowsy driving.
                 """)
        st.image(img_p7)
        st.subheader("Professional drivers")
        st.write("""
Professional drivers, such as bus drivers, taxi drivers, and delivery drivers, spend many hours on the road and may be at higher risk of experiencing drowsiness and fatigue. Driver drowsiness detection systems could help these drivers stay alert and prevent accidents.

                       """)
        st.subheader("Transportation safety advocates:")
        st.write("""
Organizations and individuals who advocate for transportation safety could be interested in promoting the adoption of driver drowsiness detection systems. These advocates may include safety groups, insurance companies, and government agencies.
""")
        st.subheader("Individuals with sleep disorders:")
        st.write("""
Individuals who suffer from sleep disorders, such as sleep apnea, may be more prone to drowsiness and could benefit from using a driver drowsiness detection system to help them stay alert while driving.
""")
        st.subheader("Families of drivers:")
        st.write("""
The families of professional drivers or individuals who frequently drive long distances may be interested in purchasing a driver drowsiness detection system as a gift or safety measure for their loved ones.

Overall, the target audience for driver drowsiness detection systems is quite broad and includes anyone who is interested in preventing accidents caused by drowsy driving.
""")
        st.write("---")




if selected == "Market-Stratagy":
    with st.container():
        st.title("Industry Relationship")
        selected = option_menu(
           menu_title ="",
           options =["Overall Criteria","Automobile Industry","Insurance Companies","Intrested Companies"],
           icons = ["pin-map","pin-map","pin-map"],
           menu_icon = "cast",
           default_index = 0)
              
        if selected == "Overall Criteria":
            st.image(img_p9)
            st.subheader("Market Overview")
            st.write("""
- The global driver drowsiness detection system market is expected to grow at a CAGR of 9.5% from 2022 to 2030.
- The growth in the market can be attributed to the increasing demand for passenger cars and commercial vehicles, and the rising awareness about road safety.
- The hardware devices segment is expected to dominate the market during the forecast period, owing to its low cost and easy installation.
- A driver drowsiness detection system is a device or software that helps to prevent drivers from falling asleep while driving.
- It monitors the driver's eyes and facial expressions to determine if they are getting sleepy.
- If it detects signs of fatigue, it will sound an alarm or take other action to wake the driver up.
- The importance of a driver drowsiness detection system is that it can help reduce the number of accidents caused by sleepy drivers.

""")
            st.subheader("Regional Analysis")
            st.image(img_p10)
            st.write("""
- North America dominated the global driver drowsiness detection system market in terms of revenue share.
- The region is expected to retain its dominance over the forecast period as well owing to increasing cases of road accidents and the growing adoption of automation across various industries, including transportation.
- Europe accounted for a significant share and is estimated to grow at a lucrative rate over the forecast period.
- This growth can be attributed to stringent government regulations regarding driving safety coupled with an increase in investments by prominent playersfor the development of advanced driver sleep systems solutions.
- Asia Pacific market was valued at USD X million and is anticipated to witness substantial growth during the forecast period owing to high incidence rates of road crashes coupled with low awareness levels among drivers about these system's benefits
- And availability of such systems on vehicles hoods ornaments or inside cabinetry panels etc.

""")
            st.subheader("Growth Factor")
            st.write("""
- Increasing demand for Driver Drowsiness Detection Systems from the automotive industry to prevent accidents caused by driver fatigue.
- Growing awareness about the benefits of using a Driver Drowsiness Detection System among consumers.
- Proliferation of advanced technologies in Driver Drowsiness Detection Systems that offer enhanced safety features.
-  Rising number of road accidents due to driver drowsiness across the globe.
- Government initiatives and regulations supporting the adoption of a Driver Drowsiness Detection System.
""")
            st.subheader("key benifits of Industries and Stakeholders")
            st.write("""

- Industry drivers, restraints, and opportunities covered in the study
- Neutral perspective on the market performance
- Recent industry trends and developments
- Competitive landscape & strategies of key players
- Potential & niche segments and regions exhibiting promising growth covered
- Historical, current, and projected market size, in terms of value
- In-depth analysis of the Driver Drowsiness Detection System Market
- The market structure and projections for the coming years.
- Drivers, restraints, opportunities, and current trends of Driver Drowsiness Detection System Market.
- Historical data and forecast.
- Estimations for the forecast period 2030.
- Developments and trends in the market.
- By Type:
      Hardware Devices
      Software System
- By Application:
      Passenger Car
      Commercial Vehicle
- Market scenario by region, sub-region, and country.

""")
            

        if selected == "Automobile Industry":
            st.subheader("Automobile Industries")
            st.image(img_p11)
            st.write("""
- It’s something that many of us have experienced while driving, though we may not like to admit it.

- It’s called a microsleep, a brief state of drowsy unconsciousness that can happen even if your eyes remain open.

- Drowsy driving kills. According to the National Highway Traffic Safety Administration, drowsy driving caused 824 deaths in 2015, the last year for which figures are available.

- Several manufacturers, including Audi, Mercedes and Volvo, currently offer drowsiness detection systems that monitor a vehicle’s movements, such as steering wheel angle, lane deviation, time driven and road conditions. 

- When drowsiness is detected, drivers are typically warned with a sound and the appearance of a coffee cup icon.

- But manufacturers and automobile suppliers are now working on advanced technological solutions that go beyond visions of coffee cups.

- To find out if drowsiness can be detected even earlier, Plessey Semiconductors has developed sensors, to be placed in a seat, that monitor changes in heart rate.

- Algorithms developed by the company indicate when breathing changes to patterns that are typical of someone who is sleeping, giving a warning before someone actually feels tired.

""")
            st.write("---")
            st.subheader("Vehicles")
            st.image(img_p12)
            st.write("""
- In addition, sensors on the outside of the vehicle will monitor the state of traffic in which the fatigued driver is engaged.
- Once vehicles can communicate with each other — a capability expected in the next few years — other cars will be able to take appropriate maneuvers toavoid the drowsy driver.
- In France, Valeo, another supplier of automotive technology, is developing an infrared camera system that will monitor children in the rear seat as well as the driver’s shoulder, neck and head movements,looking for deviations from the norm.
- Checking body temperature and even how the driver is dressed, the system will also be able to customize the interior temperature for each driver, said Guillaume Devauchelle, the company’s innovation director.
- Nvidia, chip supplier to Audi, Mercedes, Tesla and others, is developing the Co-Pilot, an artificial-intelligence tool that can learn the behaviors of individual drivers and determine when they are operating outside their norms.
- The system will eventually learn a driver’s standard posture, head position, eye-blink rate, facial expression and steering style, among other indexes.
- Based on a vehicle’s capabilities, the driver will be warned or automatically driven to a safe spot when conditions warrant.
- Until vehicles can drive themselves, it will be up to drivers to pull over once they feel drowsy.
- But drivers tend to make excuses, believing there is no danger because they are just a few minutes from home, or they are not really as tired as they may feel.
- Audi is faced with a unique problem because of its scheduled introduction next year of a car capable of driving up to 35 miles per hour without any driver intervention. When its Traffic Jam Pilot feature is engaged, the vehicle will need to determine if a driver is alert enough to take control after being a passive passenger for long periods.
- Through its Driver Availability Detection system, sensors will scan the head and face to ensure that the eyes are open and the driver is alert before the car turns over the steering wheel.
- Advanced drowsiness detection systems exist today.
- For example, Mercedes’s Attention Assist monitors a driver’s behavior for the first 20 minutes behind the wheel to get a baseline of behaviors.
- The system can currently detect drowsiness with 80 percent accuracy, said Christoph von Hugo, head of active safety for Mercedes-Benz. If drowsiness is detected, the driver is alerted to the nearest rest stop.
- For the past decade Volvo has offered its Driver Alert system. “To detect drowsiness, we study the car, not the driver,” said Mr. Aust of Volvo,
- looking at differences in the ability of the car to stay in lane, and other factors.
- The system detects drowsiness with 97 percent accuracy, Mr. Aust said.
- While N.H.T.S.A. reported 824 deaths in 2015 because of drowsiness, that number is likely to be considerably higher, the agency said.
- Drowsy driving can only be self-reported and not measured like drunkenness.
- Also, drowsiness is not reported when it is a complication of other factors like excessive drinking
- “We’re a nation of tired drivers. People talk about sleep deprivation as if it’s a badge of honor,”
- said Deborah Hersman, the head of the National Safety Council and the former chairwoman of the National Transportation Safety Board.
- “As a society we have to realize that drowsy driving is really dangerous.”
- Until fully autonomous vehicles are a reality, “drowsiness is something everyone needs to worry about,” said Mark R. Rosekind, former head of N.H.T.S.A.
- and an expert on human fatigue. “Our tendency is to say we’re wide-awake when in reality we can fall asleep in a second.”
""")
            st.write("---")
            with st.container():
                image_column,text_column = st.columns((2,1))
                st.write("##")
                with image_column:
                     st.image(img_p13)
                with text_column:
                    st.write("""
- Still, the obvious solution for a driver who feels fatigued is to pull over and rest.
- According to Mr. Rosekind, studies with airline pilots show that those who took a nap for 26 minutes improved their performance by 34 percent and alertness by 54 percent, compared with those who did not.
- Regardless of how good technology is at detecting drowsiness, fighting off sleep is futile.
- Because sleep is a biological need, the best solution for drivers is still a low-tech one: Pull over and take a nap.
""")
        if selected == "Insurance Companies":
            st.header("Insurance Companies")
            st.image(img_p14)
            st.subheader("- Insurance Companies has best market on the drowsiness detection system")
            st.subheader(" - Insurance companies are the main point to point relationship market partners")
            st.subheader(" - The driver drowsiness detection system has the data-back-up technology")
            st.subheader("- we planed the data backup in our model so this model consists of our total vedio back up of our requied data")
            st.subheader("- we can connect the data with server related to Insurance compaines ")
            st.subheader(" - so the insurance compaines has no right to claim the insurance if the accident occured due to fatigue condition of the driver")
            st.subheader(" - so hence , Insurance compaines are the best and point market partners to this model")
            st.write("---")
        if selected == "Intrested Companies":
            st.header("Some of the companies which shown intrest in this domain based on the reserach")
            st.subheader("- Continental")
            st.subheader("- Delphi Automative")
            st.subheader("- Robert Bosch")
            st.subheader("- AISIN SEIKI")
            st.subheader("- Autoliv")
            st.subheader("- DENSO")
            st.subheader("- Valeo")
            st.subheader("- manga International")
            st.subheader("- Trw Automative")
            st.subheader("- HELLA")
            st.write("---")

if selected == "Revenue":
    st.title("Revenue Generation and profits")
    selected = option_menu(
           menu_title ="",
           options =["Revenue Generation","Profits",],
           icons = ["pin-map","pin-map",],
           menu_icon = "cast",
           default_index = 0)
    
    if selected == "Revenue Generation":
        st.header("Total cost for the Product Generation")
        st.image(img_p20)
        left_column,right_column = st.columns((1,2))
        with left_column:
              st.subheader("Raspberry pi 3 Model B")
              st.write("""
- Software  Raspberry Pi 3 Model B and Raspberry Pi Camera is used because of the  high performance  of its  CPU and  higher frame  rate.
- Raspberry  Pi 3  Model  B supports  C++  and OpenCV  library.
- OpenCV  Version  3.1.0  is  applied  for various features of computer vision. The HAAR Cascade Classifier,
- warp  Affine  and  template  matching  are supported in OpenCV library.
""")
        with right_column:
              st.image(img_p15)
        st.write("---")
        left_column,right_column = st.columns((1,2))
        with left_column:
            st.subheader("Camera_Module")
            st.image(img_p16)
        with right_column:
            st.write("""
- The  main concept  of  Driver Drowsiness  Detection  is to capture  a  driver’s  eyes  from  a  camera  and  be  able  to accurately calculate the level of drowsiness in drivers with real-time processing.
- To achieve these requirements, proper materials have to be selected.
- For  the base  computer, the Raspberry Pi 3 Model B is selected.  B. System Design
""")
        st.write("---")
        left_column,right_column = st.columns((1,2))
        with left_column:
            st.subheader("Buzzer")
            st.write("""
- The buzzer is used to give the allert when the input image is matches with the image in the dataset""")
        with right_column:
            st.image(img_p17)
        st.write("---")
    if selected == "Profits":
        left_column,right_column = st.columns((1,2))
        with left_column:
            st.subheader("Automobile Industries")
            st.image(img_p18)
        with right_column:
            st.write("""
- By adding this feature to automobile the automobile sales will be increaded becaues of safety.
- The selling price of the automobile also can be raised.""")
        st.write("---")
        left_column,right_column = st.columns((1,2))
        with left_column:
            st.subheader("Insurance Companies")
            st.write("""
- By using this product , This product consists of data Backup so by this way If the accident is occured due to the drowsiness then the insurance company has no right to generate the insurance to the accident
""")
        with right_column:
            st.image(img_p19)
        st.write("---")
if selected == "Contact":
     st.header("For contacting Fill the Form we will get back you soon")
     contact_form = """
     <form action="https://formsubmit.co/vjitstudentshelpdesk@gmail.com" method="POST">
     <input type = "hidden" name ="_captcha" value = "false">
     <input type="text" name="name" placeholder = "your name" required>
     <input type="email" name="email" placeholder = "your email" required>
     <textarea name = "message" placeholder = "Compelte-details" required></textarea>
     <textarea name = "message" placeholder = "query" required></textarea>
     <button type= "submit">Send</button>
     </form>
     """
     left_column,right_column = st.columns(2)
     with left_column:
         st.markdown(contact_form,unsafe_allow_html = True)
     with right_column:
         st.empty()
    

                
            
            
          

     
    

                    
            
