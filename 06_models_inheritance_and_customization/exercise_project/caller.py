import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Mage, Necromancer, UserProfile, Message, Student


##### Exercise 1 #####

# mage = Mage.objects.create(
#     name="Fire Mage",
#     description="A powerful mage specializing in fire magic.",
#     elemental_power="Fire",
#     spellbook_type="Ancient Grimoire"
# )

# necromancer = Necromancer.objects.create(
#     name="Dark Necromancer",
#     description="A mage specializing in dark necromancy.",
#     elemental_power="Darkness", 
#     spellbook_type="Necronomicon",
#     raise_dead_ability="Raise Undead Army"
# )

# print(mage.elemental_power)
# print(mage.spellbook_type)
# print(necromancer.name)
# print(necromancer.description)
# print(necromancer.raise_dead_ability)


##### Exercise 2 #####

# user1 = UserProfile.objects.create(username='john_doe', email='john@example.com', bio='Hello, I am John Doe.')

# user2 = UserProfile.objects.create(username='jane_smith', email='jane@example.com', bio='Hi there, I am Jane Smith.')

# user3 = UserProfile.objects.create(username='alice', email='alice@example.com', bio='Hello, I am Alice.')

# # Create a message from user1 to user2
# message1 = Message.objects.create(
#     sender=user1,
#     receiver=user2,
#     content="Hello, Jane! Could you please tell Alice that tomorrow we are going on vacation?")

# # Display the content
# print(message1.content)

# # Mark the message as read
# message1.mark_as_read()
# print(f"Is read: {message1.is_read}")

# # Create a reply from user2 to user1
# reply_message = message1.reply_to_message(
#     reply_content="Hi John, sure! I will forward this message to her!")

# # Display the content
# print(reply_message.content)

# # Create a forwarded message from user2 to user3
# forwarded_message = message1.forward_message(receiver=user3)

# print(f"Forwarded message from {forwarded_message.sender.username} to {forwarded_message.receiver.username}")


##### Exercise 3 #####

# student1 = Student(name="Alice", student_id=45.23)
# student1.full_clean()
# student1.save()
# retrieved_student1 = Student.objects.get(name="Alice")

# Print the saved ID of the student1
# print(retrieved_student1.student_id)

# Try to parse zero as ID and expect ValueError
# try:
#     student2 = Student(name="Bob", student_id="0")
#     student1.full_clean()
#     student2.save()
# except ValueError as error:
#     print(error)