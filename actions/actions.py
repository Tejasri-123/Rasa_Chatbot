# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action , Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List



class ActionProvideSyllabus(Action):
    def name(self):
        return "action_provide_syllabus"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        subject = tracker.get_slot("subject")

        if not subject:
            dispatcher.utter_message(response="utter_ask_subject")
            return []

        # Dictionary with GATE syllabus PDF links
        syllabus_links = {
            "aerospace engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/ae.pdf",
            "agricultural engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/ag.pdf",
            "architecture and planning": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/ar.pdf",
            "biomedical engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/bm.pdf",
            "biotechnology": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/bt.pdf",
            "civil engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/ce.pdf",
            "chemical engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/ch.pdf",
            "computer science and information technology": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/cs.pdf",
            "chemistry": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/cy.pdf",
            "electronics and communication engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/ec.pdf",
            "electrical engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/ee.pdf",
            "environmental science and engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/es.pdf",
            "ecology and evolution": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/ey.pdf",
            "geomatics engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/ge.pdf",
            "geology and geophysics": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/gg.pdf",
            "instrumentation engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/in.pdf",
            "mathematics": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/ma.pdf",
            "mechanical engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/me.pdf",
            "mining engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/mn.pdf",
            "metallurgical engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/mt.pdf",
            "naval architecture and marine engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/na.pdf",
            "petroleum engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/pe.pdf",
            "physics": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/ph.pdf",
            "production and industrial engineering": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/pi.pdf",
            "statistics": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/st.pdf",
            "textile engineering and fibre science": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/tf.pdf",
            "engineering sciences": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/xe.pdf",
            "humanities and social sciences": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/xh.pdf",
            "life sciences": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/xl.pdf",
            "data science and artificial intelligence": "https://gate.iitk.ac.in/GATE2023/doc/Syllabus/da.pdf"
        }

        subject_key = subject.lower().strip()

        if subject_key in syllabus_links:
            pdf_link = syllabus_links[subject_key]
            dispatcher.utter_message(text=f"📚 Here is the GATE syllabus for <b>{subject.title()}</b>: <a href='{pdf_link}' target='_blank'>Download PDF</a>")
        else:
            dispatcher.utter_message(text=f"❗ Sorry, I couldn't find the syllabus for <b>{subject.title()}</b>. Please check the official GATE website for more information: <a href='https://gate2025.iitr.ac.in/' target='_blank'>GATE Official Website</a>")
        
        return [SlotSet("subject", subject)]

#########################################################################################################



# Dictionary containing important topics for each subject
important_topics = {
    "Aerospace Engineering": ["Aerodynamics", "Propulsion", "Structures", "Flight Mechanics"],
    "Agricultural Engineering": ["Soil and Water Engineering", "Farm Machinery", "Renewable Energy"],
    "Architecture and Planning": ["Urban Planning", "Building Materials", "Sustainable Design"],
    "Biomedical Engineering": ["Biomechanics", "Medical Imaging", "Biomedical Signal Processing"],
    "Biotechnology": ["Genetic Engineering", "Bioprocess Engineering", "Microbiology"],
    "Civil Engineering": ["Structural Engineering", "Geotechnical Engineering", "Transportation Engineering"],
    "Chemical Engineering": ["Process Calculations", "Fluid Mechanics", "Mass Transfer Operations"],
    "Computer Science and Information Technology": ["Data Structures", "Algorithms", "Operating Systems", "Database Management"],
    "Chemistry": ["Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry"],
    "Electronics and Communication Engineering": ["Analog Circuits", "Digital Electronics", "Communication Systems"],
    "Electrical Engineering": ["Power Systems", "Control Systems", "Electrical Machines"],
    "Environmental Science and Engineering": ["Environmental Chemistry", "Water and Waste Management", "Air Pollution"],
    "Ecology and Evolution": ["Evolutionary Biology", "Ecological Dynamics", "Conservation Biology"],
    "Geomatics Engineering": ["Geodesy", "Remote Sensing", "GIS Applications"],
    "Geology and Geophysics": ["Mineralogy", "Petrology", "Seismology"],
    "Instrumentation Engineering": ["Sensors and Transducers", "Industrial Instrumentation", "Control Systems"],
    "Mathematics": ["Linear Algebra", "Calculus", "Probability and Statistics"],
    "Mechanical Engineering": ["Thermodynamics", "Fluid Mechanics", "Machine Design"],
    "Mining Engineering": ["Mine Ventilation", "Rock Mechanics", "Surface Mining"],
    "Metallurgical Engineering": ["Extractive Metallurgy", "Physical Metallurgy", "Material Characterization"],
    "Naval Architecture and Marine Engineering": ["Ship Design", "Marine Hydrodynamics", "Structural Analysis"],
    "Petroleum Engineering": ["Reservoir Engineering", "Drilling Engineering", "Petroleum Production"],
    "Physics": ["Classical Mechanics", "Quantum Mechanics", "Electromagnetism"],
    "Production and Industrial Engineering": ["Manufacturing Processes", "Operations Research", "Quality Control"],
    "Statistics": ["Probability Theory", "Regression Analysis", "Hypothesis Testing"],
    "Textile Engineering and Fibre Science": ["Textile Fibers", "Yarn Production", "Textile Chemistry"],
    "Engineering Sciences": ["Material Science", "Applied Mechanics", "Fluid Dynamics"],
    "Humanities and Social Sciences": ["Sociology", "Psychology", "Political Science"],
    "Life Sciences": ["Cell Biology", "Genetics", "Biochemistry"],
    "Data Science and Artificial Intelligence": ["Machine Learning", "Deep Learning", "Natural Language Processing"]
}

class ActionProvideImportantTopics(Action):

    def name(self) -> Text:
        return "action_provide_important_topics"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        subject = next(tracker.get_latest_entity_values("subject"), None)
        
        if subject and subject in important_topics:
            topics = "".join([f"<li>{topic}</li>" for topic in important_topics[subject]])
            dispatcher.utter_message(text=f"""<h3>📌 Important Topics in {subject.capitalize()}</h3>
            <ul>{topics}</ul>""")
        else:
            dispatcher.utter_message(text=f"<p>❗ Sorry, I don't have information about the important topics for <strong>{subject}</strong>. Please check the subject name or try again.</p>")
        
        return []
    
#######################################################################
class ActionProvideRoadmap(Action):
    def name(self) -> str:
        return "action_provide_roadmap"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        duration = tracker.get_slot('duration')
        print(f"Captured Duration: {duration}")  # Debugging line

        if duration == "1 year":
            message = (
                "<h2>📚 1-Year GATE Preparation Roadmap</h2>"
                "<h3>Phase 1: First 4 Months - Strong Foundation</h3>"
                "<ul>"
                "<li>✅ Complete the GATE syllabus by dedicating sufficient time to core subjects.</li>"
                "<li>✅ Study Mathematics and Aptitude simultaneously, as they are scoring.</li>"
                "<li>✅ Refer to standard textbooks and online resources.</li>"
                "<li>✅ Solve conceptual and numerical problems regularly.</li>"
                "</ul>"
                "<h3>Phase 2: Next 3 Months - Practice and Analysis</h3>"
                "<ul>"
                "<li>✅ Start practicing previous years’ GATE papers.</li>"
                "<li>✅ Take chapter-wise and subject-wise mock tests.</li>"
                "<li>✅ Analyze mistakes and revise weak areas.</li>"
                "<li>✅ Prepare short notes and formula sheets.</li>"
                "</ul>"
                "<h3>Phase 3: Last 5 Months - Revision and Full-Length Tests</h3>"
                "<ul>"
                "<li>✅ Attempt full-length mock tests every week.</li>"
                "<li>✅ Time yourself and improve accuracy.</li>"
                "<li>✅ Revise thoroughly using short notes and flashcards.</li>"
                "<li>✅ Manage stress and practice mindfulness.</li>"
                "<li>✅ Stay consistent and confident! 🎯</li>"
                "</ul>"
       )
        elif duration == "6 months":
            message = (
                "<h2>📚 6-Month GATE Preparation Roadmap</h2>"
                "<h3>Phase 1: First 2 Months - Rapid Learning</h3>"
                "<ul>"
                "<li>✅ Focus on understanding core concepts.</li>"
                "<li>✅ Divide subjects strategically, covering 2-3 topics weekly.</li>"
                "<li>✅ Make short notes for quick revision.</li>"
                "<li>✅ Solve simple and moderate-level problems daily.</li>"
                "</ul>"
                "<h3>Phase 2: Next 2 Months - Practice and Improve</h3>"
                "<ul>"
                "<li>✅ Start practicing previous years’ GATE papers.</li>"
                "<li>✅ Attempt chapter-wise and subject-wise tests.</li>"
                "<li>✅ Analyze performance and revisit difficult topics.</li>"
                "<li>✅ Develop a problem-solving approach.</li>"
                "</ul>"
                "<h3>Phase 3: Last 2 Months - Intensive Practice</h3>"
                "<ul>"
                "<li>✅ Take 10-12 full-length mock tests.</li>"
                "<li>✅ Practice under timed conditions.</li>"
                "<li>✅ Strengthen weaker sections through targeted revision.</li>"
                "<li>✅ Maintain exam-day strategy and mental calmness.</li>"
                "<li>✅ Believe in yourself and stay positive! 🌟</li>"
                "</ul>"
            )

        elif duration == "3 months":
            
            message = (
                "<h2>📚 3-Month GATE Crash Course</h2>"
                "<h3>Phase 1: First 1 Month - Focus on High-Weightage Topics</h3>"
                "<ul>"
                "<li>✅ Identify high-weightage subjects using previous year analysis.</li>"
                "<li>✅ Prioritize Mathematics, Aptitude, and core subjects.</li>"
                "<li>✅ Study 8-10 hours a day with effective time management.</li>"
                "<li>✅ Practice conceptual and application-based questions.</li>"
                "</ul>"
                "<h3>Phase 2: Second Month - Intensive Practice</h3>"
                "<ul>"
                "<li>✅ Solve previous years’ papers daily.</li>"
                "<li>✅ Take subject-wise mock tests every week.</li>"
                "<li>✅ Focus on time management and accuracy.</li>"
                "<li>✅ Identify weak areas and strengthen them.</li>"
                "</ul>"
                "<h3>Phase 3: Final Month - Revision and Final Push</h3>"
                "<ul>"
                "<li>✅ Revise using short notes and formula sheets.</li>"
                "<li>✅ Attempt full-length mock tests under timed conditions.</li>"
                "<li>✅ Maintain a balanced study schedule with sufficient breaks.</li>"
                "<li>✅ Stay motivated and confident. Success is near! 🚀</li>"
                "</ul>"
    )
            
        else:
            message = (
            "<p>❗ <b>I couldn't understand the period you provided.</b></p>"
            "<p>Please specify one of the following options:</p>"
            "<ul>"
            "<li>📅 <b>1 year</b></li>"
            "<li>📅 <b>6 months</b></li>"
            "<li>📅 <b>3 months</b></li>"
            "</ul>"
        )

        dispatcher.utter_message(text=message)
        return []


        
       


class ActionProvideTips(Action):
    def name(self) -> str:
        return "action_provide_tips"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        tips = (
            "<p>📝 <b>GATE Preparation Tips:</b></p>"
            "<ul>"
            "<li>📅 Make a realistic timetable and stick to it.</li>"
            "<li>🧑‍💻 Focus on understanding concepts rather than rote learning.</li>"
            "<li>📚 Practice previous year papers and mock tests.</li>"
            "<li>🔎 Analyze your mistakes and work on weak areas.</li>"
            "<li>🧘 Take regular breaks and stay consistent.</li>"
            "<li>⏰ Manage your time effectively during the exam.</li>"
            "</ul>"
        )


        dispatcher.utter_message(text=tips)
        return []
    
#######################################################################################

class ActionProvideResources(Action):
    def name(self) -> Text:
        return "action_provide_resources"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        subject = tracker.get_slot('subject')

        resources = {
            "Aerospace Engineering": "<b>📚 Books:</b> Introduction to Flight by John Anderson.<br><b>💻 Online Courses:</b> NPTEL Aerospace Lectures.<br><b>🧑‍💻 Practice:</b> GATE Overflow.",

            "Agricultural Engineering": "<b>📚 Books:</b> Fundamentals of Soil Science by Henry D. Foth.<br><b>💻 Online Courses:</b> ICAR eCourses.<br><b>🧑‍💻 Practice:</b> AgriGATE Test Series.",

            "Architecture and Planning": "<b>📚 Books:</b> Planning for Sustainability by Stephen Wheeler.<br><b>💻 Online Courses:</b> NPTEL Urban Planning.<br><b>🧑‍💻 Practice:</b> Made Easy Series.",

            "Biomedical Engineering": "<b>📚 Books:</b> Biomedical Engineering Handbook by Joseph D. Bronzino.<br><b>💻 Online Courses:</b> MIT OpenCourseWare.<br><b>🧑‍💻 Practice:</b> Biomed GATE Series.",

            "Biotechnology": "<b>📚 Books:</b> Molecular Biology of the Cell by Alberts.<br><b>💻 Online Courses:</b> Coursera Biotechnology Courses.<br><b>🧑‍💻 Practice:</b> GATEForum Biotechnology.",

            "Civil Engineering": "<b>📚 Books:</b> Strength of Materials by R.K. Bansal.<br><b>💻 Online Courses:</b> IIT Kharagpur NPTEL Lectures.<br><b>🧑‍💻 Practice:</b> Made Easy Test Series.",

            "Chemical Engineering": "<b>📚 Books:</b> Mass Transfer Operations by Treybal.<br><b>💻 Online Courses:</b> NPTEL Chemical Engineering Lectures.<br><b>🧑‍💻 Practice:</b> Testbook Chemical Series.",

            "Computer Science and Information Technology": "<b>📚 Books:</b> Introduction to Algorithms by Cormen (CLRS).<br><b>💻 Online Courses:</b> NPTEL Computer Science Series.<br><b>🧑‍💻 Practice:</b> GeeksforGeeks, LeetCode.",

            "Chemistry": "<b>📚 Books:</b> Organic Chemistry by Morrison & Boyd.<br><b>💻 Online Courses:</b> Khan Academy Chemistry.<br><b>🧑‍💻 Practice:</b> Chemistry GATE Mock Tests.",

            "Electrical Engineering": "<b>📚 Books:</b> Electrical Machines by P.S. Bimbhra.<br><b>💻 Online Courses:</b> NPTEL Electrical Engineering.<br><b>🧑‍💻 Practice:</b> Ace Academy Test Series.",
            
            "Electronics and Communication Engineering": "<b>📚 Books:</b> Microelectronics by Sedra and Smith.<br><b>💻 Online Courses:</b> Udemy GATE ECE Courses.<br><b>🧑‍💻 Practice:</b> GateOverflow.",

            "Environmental Science and Engineering": "<b>📚 Books:</b> Environmental Engineering by Peavy and Rowe.<br><b>💻 Online Courses:</b> NPTEL Environmental Studies.<br><b>🧑‍💻 Practice:</b> Testbook Environmental Series.",

            "Ecology and Evolution": "<b>📚 Books:</b> Ecology by Odum.<br><b>💻 Online Courses:</b> Coursera Evolution Courses.<br><b>🧑‍💻 Practice:</b> GATE Ecology Test Series.",

            "Geomatics Engineering": "<b>📚 Books:</b> Surveying by B.C. Punmia.<br><b>💻 Online Courses:</b> NPTEL Geomatics.<br><b>🧑‍💻 Practice:</b> GATEForum Geomatics Series.",

            "Geology and Geophysics": "<b>📚 Books:</b> Earth Science by Tarbuck.<br><b>💻 Online Courses:</b> NPTEL Geophysics Lectures.<br><b>🧑‍💻 Practice:</b> Testbook Geology Series.",

            "Instrumentation Engineering": "<b>📚 Books:</b> Measurements and Instrumentation by A.K. Sawhney.<br><b>💻 Online Courses:</b> NPTEL Measurement & Instrumentation Series.<br><b>🧑‍💻 Practice:</b> GateForum Test Series.",

            "Mathematics": "<b>📚 Books:</b> Higher Engineering Mathematics by B.S. Grewal.<br><b>💻 Online Courses:</b> Khan Academy.<br><b>🧑‍💻 Practice:</b> Made Easy Test Series.",

            "Mechanical Engineering": "<b>📚 Books:</b> Engineering Thermodynamics by PK Nag.<br><b>💻 Online Courses:</b> NPTEL Mechanical Lectures.<br><b>🧑‍💻 Practice:</b> GATE Overflow.",

            "Mining Engineering": "<b>📚 Books:</b> Elements of Mining Technology by D.J. Deshmukh.<br><b>💻 Online Courses:</b> NPTEL Mining Engineering.<br><b>🧑‍💻 Practice:</b> GATE Mining Series.",

            "Metallurgical Engineering": "<b>📚 Books:</b> Introduction to Metallurgy by Sidney Avner.<br><b>💻 Online Courses:</b> NPTEL Metallurgy Courses.<br><b>🧑‍💻 Practice:</b> Metallurgy GATE Practice Tests.",

            "Naval Architecture and Marine Engineering": "<b>📚 Books:</b> Principles of Naval Architecture by Edward V. Lewis.<br><b>💻 Online Courses:</b> NPTEL Naval Engineering.<br><b>🧑‍💻 Practice:</b> Testbook Marine Series.",

            "Petroleum Engineering": "<b>📚 Books:</b> Petroleum Refining by James H. Gary.<br><b>💻 Online Courses:</b> NPTEL Petroleum Courses.<br><b>🧑‍💻 Practice:</b> GATE Petroleum Test Series.",

            "Physics": "<b>📚 Books:</b> Concepts of Physics by HC Verma.<br><b>💻 Online Courses:</b> MIT OpenCourseWare Physics Series.<br><b>🧑‍💻 Practice:</b> GATE Physics Study Group.",

            "Production and Industrial Engineering": "<b>📚 Books:</b> Industrial Engineering and Management by OP Khanna.<br><b>💻 Online Courses:</b> NPTEL Production Engineering.<br><b>🧑‍💻 Practice:</b> Testbook Industrial Series.",

            "Statistics": "<b>📚 Books:</b> Probability and Statistics by Jay L. Devore.<br><b>💻 Online Courses:</b> Khan Academy Statistics.<br><b>🧑‍💻 Practice:</b> Statistics GATE Mock Tests.",

            "Textile Engineering and Fibre Science": "<b>📚 Books:</b> Textile Science by Corbman.<br><b>💻 Online Courses:</b> NPTEL Textile Courses.<br><b>🧑‍💻 Practice:</b> Textile GATE Series.",

            "Engineering Sciences": "<b>📚 Books:</b> Engineering Science by Michael Higgins.<br><b>💻 Online Courses:</b> NPTEL Engineering Sciences.<br><b>🧑‍💻 Practice:</b> Made Easy Test Series.",
        
            "Humanities and Social Sciences": "<b>📚 Books:</b> Social Sciences by David C. Colander.<br><b>💻 Online Courses:</b> NPTEL Humanities Courses.<br><b>🧑‍💻 Practice:</b> GATE Humanities Series.",

            "Life Sciences": "<b>📚 Books:</b> Life Sciences by Gerald Karp.<br><b>💻 Online Courses:</b> EdX Life Sciences.<br><b>🧑‍💻 Practice:</b> Life Sciences GATE Prep Tests.",

            "Data Science and Artificial Intelligence": "<b>📚 Books:</b> Hands-On Machine Learning by Aurélien Géron.<br><b>💻 Online Courses:</b> Coursera Data Science.<br><b>🧑‍💻 Practice:</b> Kaggle Competitions."

        }

        if subject in resources:
            dispatcher.utter_message(text=resources[subject])
        else:
            dispatcher.utter_message(text="<b>⚠️ Sorry!</b> I don't have resources for that subject. Please try another subject or check back later.")

        return []
