import pygame


class Node:
    """Tree node"""
    def __init__(self, data, description, move_node=False):
        self.data = data
        self.description = description
        self.parent = None
        self.children = []
        self.move_node = move_node
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)


#Tile: 
# type
# list of actions
# image
# position


class Tile:
    def __init__(self, type, actions, image, position):
        """Map tile"""
        self.type = type
        self.actions = actions
        self.image = image
        self.position = position

class Forest(Tile):
    def __init__(self, position):
        self.type = 'Forest'
        self.actions = {''}
        self.image = pygame.image.load('assets/forest.png')

        #------------ Exit ------------  Done
        
        exitactivity = Node("leave", "As you find your way out of the forest you go...", move_node=True)

        #------------ Gather ------------  Done

        sub_sub_activity1_1 = Node("yes", "you taste some of the liquid gel and it does not taste of anything, however the chew is satisfying and you chew on some like gum for a bit, what do you do now?")
        sub_sub_activity1_2 = Node("no", "you leave the liquid, what do you do?")
        sub_sub_activity1_1.add_child(exitactivity)
        sub_sub_activity1_2.add_child(exitactivity)

        sub_activity1 = Node("gel", "you see a liquid gel pouring out of the bark on a tree, do you taste it?")
        sub_activity1.add_child(sub_sub_activity1_1)
        sub_activity1.add_child(sub_sub_activity1_2)

        sub_sub_activity2_1 = Node("yes", "you dig it up and find a steel sword, with a hilt, you strap on the hilt and put the sword in it, what do you do?")
        sub_sub_activity2_2 = Node("no", "you leave the shiny object, what do you do?")
        sub_sub_activity2_1.add_child(exitactivity)
        sub_sub_activity2_2.add_child(exitactivity)

        sub_activity2 = Node("shiny", "you see a small portion of a shiony object covered in moss, do you dig it up?")
        sub_activity2.add_child(sub_sub_activity2_1)
        sub_activity2.add_child(sub_sub_activity2_2)

        sub_sub_activity3_1 = Node("yes", "you take some of the moss with you in your bag, what do you do?")
        sub_sub_activity3_2 = Node("no", "you leave the moss, what do you do?")
        sub_sub_activity3_1.add_child(exitactivity)
        sub_sub_activity3_2.add_child(exitactivity)

        sub_activity3 = Node("moss", "you see a type of yellow moss on the ground, do you take some of it?")
        sub_activity3.add_child(sub_sub_activity3_1)
        sub_activity3.add_child(sub_sub_activity3_2)

        activity1 = Node("gather", "as you walk around in the forest you see an array of possibly useful materials laying around, which one do you take?")
        activity1.add_child(sub_activity1)
        activity1.add_child(sub_activity2)
        activity1.add_child(sub_activity3)

        #------------ Research ------------  Done

        sub_sub_activity4_1 = Node("leave it", "you leave the mushrrom, what do you do?")
        sub_sub_activity4_2 = Node("pick it", "you take the mushrrom, what do you do?")
        sub_sub_activity4_1.add_child(exitactivity)
        sub_sub_activity4_2.add_child(exitactivity)

        sub_activity4 = Node("feel", "you feel the mushrooms slimy outer and open it and feel the moist inside, do you pick more mushrooms?")
        sub_activity4.add_child(sub_sub_activity4_1)
        sub_activity4.add_child(sub_sub_activity4_2)

        sub_sub_activity5_1 = Node("leave it", "you leave the mushrrom, what do you do?")
        sub_sub_activity5_2 = Node("pick it", "you take the mushrrom, what do you do?")
        sub_sub_activity5_1.add_child(exitactivity)
        sub_sub_activity5_2.add_child(exitactivity)

        sub_activity5 = Node("lick", "as you lick the mushroom it gives of an earthy taste and your tongue begins to feel irritated, what do you do?")
        sub_activity5.add_child(sub_sub_activity5_1)
        sub_activity5.add_child(sub_sub_activity5_2)

        sub_sub_activity6_1 = Node("leave it", "you leave the mushroom, what do you do?")
        sub_sub_activity6_2 = Node("pick it", "you take the mushroom, what do you do?")
        sub_sub_activity6_1.add_child(exitactivity)
        sub_sub_activity6_2.add_child(exitactivity)

        sub_activity6 = Node("taste", "you taste the mushroom and as the mushroom hits you tongue it tastes slimy and earthy, what do you do?")
        sub_activity6.add_child(sub_sub_activity6_1)
        sub_activity6.add_child(sub_sub_activity6_2)

        activity2 = Node("research", 'You walk along a path in the forest, and as you do this all kinds of different plants can be found and you come across a brown mushroom, what do you do?')
        activity2.add_child(sub_activity4)
        activity2.add_child(sub_activity5)
        activity2.add_child(sub_activity6)

        #------------ Cabin ------------  Done

        sub_sub_activity7_1 = Node("yes", "you walk further into the darkness and do no find anything. you leave the cellar, what do you do now?")
        sub_sub_activity7_2 = Node("no", "you go out of the cellar, what do you do?")
        sub_sub_activity7_1.add_child(exitactivity)
        sub_sub_activity7_2.add_child(exitactivity)

        sub_activity7 = Node("cellar", "as you enter the cellar it is really dark, do you venture further?")
        sub_activity7.add_child(sub_sub_activity7_1)
        sub_activity7.add_child(sub_sub_activity7_2)

        sub_sub_activity8_1 = Node("speak", "you try to speak to the figure, it screeches as it hears your voice, you leave the room in fear, what do you do?")
        sub_sub_activity8_2 = Node("leave", "you exit the room, what do you do?")
        sub_sub_activity8_1.add_child(exitactivity)
        sub_sub_activity8_2.add_child(exitactivity)

        sub_activity8 = Node("kitchen", "you walk into the kitchen and see a dark long lanky figure, what do you do?")
        sub_activity8.add_child(sub_sub_activity8_1)
        sub_activity8.add_child(sub_sub_activity8_2)

        sub_sub_activity9_1 = Node("lighter", "you grab the lighter and leave the room, what do you do?")
        sub_sub_activity9_2 = Node("flashlight", "you grab the lighter and leave the room, what do you do?")
        sub_sub_activity9_1.add_child(exitactivity)
        sub_sub_activity9_2.add_child(exitactivity)

        sub_activity9 = Node("bedroom", "You enter the bedroom and see a flashlight and a lighter, which do you take?")
        sub_activity9.add_child(sub_sub_activity9_1)
        sub_activity9.add_child(sub_sub_activity9_2)

        activity3 = Node("cabin", "You open the door to the cabin and see a kitchen door, a cellar door and a bedroom door, which room do you enter?")
        activity3.add_child(sub_activity7)
        activity3.add_child(sub_activity8)
        activity3.add_child(sub_activity9)

        #------------ Root ------------  Done

        self.root = Node("forest", "As you walk into the forest you see a log cabin, it looks old and abandoned and has moss growing all over the roof of it. What do you do?", move_node=False)
        self.root.add_child(activity1)
        self.root.add_child(activity2)
        self.root.add_child(activity3)

class Mountain(Tile):
    def __init__(self, position):
        self.type = 'Mountain'
        self.actions = {''}
        self.image = pygame.image.load('assets/mountain.png')
        
        #------------ Exit ------------  Done
        
        exitactivity = Node("leave", "As you find your way out of the mounatin you go...", move_node=True)

        #------------ Gather ------------  Done

        sub_sub_activity1_1 = Node("yes", "you take the piece of flint and put it in your backpack, what do you do now?")
        sub_sub_activity1_2 = Node("no", "you leave the flint, what do you do?")
        sub_sub_activity1_1.add_child(exitactivity)
        sub_sub_activity1_2.add_child(exitactivity)

        sub_activity1 = Node("flint", "you see a piece of flint in the wall of the mountain, do you take it?")
        sub_activity1.add_child(sub_sub_activity1_1)
        sub_activity1.add_child(sub_sub_activity1_2)

        sub_sub_activity2_1 = Node("yes", "you dig it up and put it in your backpack, what do you do?")
        sub_sub_activity2_2 = Node("no", "you leave the brown rock, what do you do?")
        sub_sub_activity2_1.add_child(exitactivity)
        sub_sub_activity2_2.add_child(exitactivity)

        sub_activity2 = Node("brown rock", "you see a brown rock that looks like iron, do you dig it up?")
        sub_activity2.add_child(sub_sub_activity2_1)
        sub_activity2.add_child(sub_sub_activity2_2)

        sub_sub_activity3_1 = Node("yes", "you dig up the shiny object and it is a steel body armour, it looks good so you equip it, what do you do?")
        sub_sub_activity3_2 = Node("no", "you leave the object, what do you do?")
        sub_sub_activity3_1.add_child(exitactivity)
        sub_sub_activity3_2.add_child(exitactivity)

        sub_activity3 = Node("shiny", "you see a shiny object covered in rocks, do you dig it up?")
        sub_activity3.add_child(sub_sub_activity3_1)
        sub_activity3.add_child(sub_sub_activity3_2)

        activity1 = Node("gather", "as you walk around in the forest you see an array of possibly useful materials laying around, which one do you take?")
        activity1.add_child(sub_activity1)
        activity1.add_child(sub_activity2)
        activity1.add_child(sub_activity3)

        #------------ Research ------------  Done

        sub_sub_activity4_1 = Node("leave it", "you leave the rock, what do you do?")
        sub_sub_activity4_2 = Node("pick it", "you take the rock and put it in your backpack, what do you do then?")
        sub_sub_activity4_1.add_child(exitactivity)
        sub_sub_activity4_2.add_child(exitactivity)

        sub_activity4 = Node("feel", "you feel the shiny rock and it seems very hard, what do you do?")
        sub_activity4.add_child(sub_sub_activity4_1)
        sub_activity4.add_child(sub_sub_activity4_2)

        sub_sub_activity5_1 = Node("leave it", "you leave the rock, what do you do?")
        sub_sub_activity5_2 = Node("pick it", "you take the rock and put it in your backpack, what do you do?")
        sub_sub_activity5_1.add_child(exitactivity)
        sub_sub_activity5_2.add_child(exitactivity)

        sub_activity5 = Node("lick", "as you lick the rock and it has a very irony taste to it, what do you do?")
        sub_activity5.add_child(sub_sub_activity5_1)
        sub_activity5.add_child(sub_sub_activity5_2)

        sub_sub_activity6_1 = Node("leave it", "you leave the rock, what do you do?")
        sub_sub_activity6_2 = Node("pick it", "you take the rock and put it in your backpack, what do you do?")
        sub_sub_activity6_1.add_child(exitactivity)
        sub_sub_activity6_2.add_child(exitactivity)

        sub_activity6 = Node("bite", "you take a bite of the shiny rock and one of your teeth starts to shatter, what do you do?")
        sub_activity6.add_child(sub_sub_activity6_1)
        sub_activity6.add_child(sub_sub_activity6_2)

        activity2 = Node("research", 'you see a small very shiny piece of rock sticking out from the mountain wall, what do you do?')
        activity2.add_child(sub_activity4)
        activity2.add_child(sub_activity5)
        activity2.add_child(sub_activity6)

        #------------ Quarry ------------  Done

        sub_sub_activity7_1 = Node("yes", "you press the button and the machinery turns on for a moment, but then explodes making a log fly onto your foot hurting the foot pretty badly, what do you do now?")
        sub_sub_activity7_2 = Node("no", "you exit the quarry, what do you do?")
        sub_sub_activity7_1.add_child(exitactivity)
        sub_sub_activity7_2.add_child(exitactivity)

        sub_activity7 = Node("machinery", "the machinery seems old and has some buttons, but one button is red and sticks out from the rest, do you press it?")
        sub_activity7.add_child(sub_sub_activity7_1)
        sub_activity7.add_child(sub_sub_activity7_2)

        sub_sub_activity8_1 = Node("remove", "you remove the big pile and reveal an old script on the wall behind it in some ancient language, what do you do?")
        sub_sub_activity8_2 = Node("leave", "you exit the quarry, what do you do?")
        sub_sub_activity8_1.add_child(exitactivity)
        sub_sub_activity8_2.add_child(exitactivity)

        sub_activity8 = Node("logs", "you see a pile of logs, what do you do?")
        sub_activity8.add_child(sub_sub_activity8_1)
        sub_activity8.add_child(sub_sub_activity8_2)

        sub_sub_activity9_1 = Node("jacket", "you grab the jacket and leave the quarry, what do you do?")
        sub_sub_activity9_2 = Node("pickaxe", "you grab the pickaxe and leave the quarry, what do you do?")
        sub_sub_activity9_1.add_child(exitactivity)
        sub_sub_activity9_2.add_child(exitactivity)

        sub_activity9 = Node("equipment", "You see an old jacket and a pickaxe, which do you take?")
        sub_activity9.add_child(sub_sub_activity9_1)
        sub_activity9.add_child(sub_sub_activity9_2)

        activity3 = Node("qaurry", "you see a quarry with some old equipment, logs and some type of machinery, what do you do??")
        activity3.add_child(sub_activity7)
        activity3.add_child(sub_activity8)
        activity3.add_child(sub_activity9)

        #------------ Root ------------  Done

        self.root = Node("mountain", "As you walk along the mountain you see a mountain pass and a quarry. What do you do?", move_node=False)
        self.root.add_child(activity1)
        self.root.add_child(activity2)
        self.root.add_child(activity3)

class River(Tile):
    def __init__(self, position):
        self.type = 'River'
        self.actions = {''}
        self.image = pygame.image.load('assets/river.png')
        
        #------------ Exit ------------  Done
        
        exitactivity = Node("leave", "As you find your way away from the river you go...", move_node=True)

        #------------ Gather ------------  Done

        sub_sub_activity1_1 = Node("yes", "you take the stick and put it in your backpack, what do you do now?")
        sub_sub_activity1_2 = Node("no", "you leave the stick, what do you do?")
        sub_sub_activity1_1.add_child(exitactivity)
        sub_sub_activity1_2.add_child(exitactivity)

        sub_activity1 = Node("stick", "you see a pickup a blue stick from the water and it feels durable, do you take it?")
        sub_activity1.add_child(sub_sub_activity1_1)
        sub_activity1.add_child(sub_sub_activity1_2)

        sub_sub_activity2_1 = Node("yes", "you dig it up and put it in your backpack, what do you do?")
        sub_sub_activity2_2 = Node("no", "you leave the plant, what do you do?")
        sub_sub_activity2_1.add_child(exitactivity)
        sub_sub_activity2_2.add_child(exitactivity)

        sub_activity2 = Node("aloe", "you see a plant tha looks like aloe, do you take it?")
        sub_activity2.add_child(sub_sub_activity2_1)
        sub_activity2.add_child(sub_sub_activity2_2)

        sub_sub_activity3_1 = Node("yes", "you equip the shield, what do you do?")
        sub_sub_activity3_2 = Node("no", "you leave the object, what do you do?")
        sub_sub_activity3_1.add_child(exitactivity)
        sub_sub_activity3_2.add_child(exitactivity)

        sub_activity3 = Node("shiny", "you see a shiny object in the water and as you dig it up it is a shield, do you take it?")
        sub_activity3.add_child(sub_sub_activity3_1)
        sub_activity3.add_child(sub_sub_activity3_2)

        activity1 = Node("gather", "You walk along the edge of the river and see some plant, a shiny object in the river and some weird water sticks, which one do you take?")
        activity1.add_child(sub_activity1)
        activity1.add_child(sub_activity2)
        activity1.add_child(sub_activity3)

        #------------ Research ------------  Done

        sub_sub_activity4_1 = Node("leave it", "you leave the algae, what do you do?")
        sub_sub_activity4_2 = Node("pick it", "you take the algae and put it in your backpack, what do you do then?")
        sub_sub_activity4_1.add_child(exitactivity)
        sub_sub_activity4_2.add_child(exitactivity)

        sub_activity4 = Node("feel", "you feel the algae and it does not feel very good, what do you do?")
        sub_activity4.add_child(sub_sub_activity4_1)
        sub_activity4.add_child(sub_sub_activity4_2)

        sub_sub_activity5_1 = Node("leave it", "you leave the algae, what do you do?")
        sub_sub_activity5_2 = Node("take it", "you take the algae and put it in your backpack, what do you do?")
        sub_sub_activity5_1.add_child(exitactivity)
        sub_sub_activity5_2.add_child(exitactivity)

        sub_activity5 = Node("lick", "as you lick the algae it tastes like nothing you have ever tasted befre, what do you do?")
        sub_activity5.add_child(sub_sub_activity5_1)
        sub_activity5.add_child(sub_sub_activity5_2)

        sub_sub_activity6_1 = Node("take more", "you take some more algae and put it in your backpack, what do you do?")
        sub_sub_activity6_2 = Node("leave it", "you leave the algae, what do you do?")
        sub_sub_activity6_1.add_child(exitactivity)
        sub_sub_activity6_2.add_child(exitactivity)

        sub_activity6 = Node("bite", "you take a bite of the algae and it is unbelievably good, what do you do?")
        sub_activity6.add_child(sub_sub_activity6_1)
        sub_activity6.add_child(sub_sub_activity6_2)

        activity2 = Node("research", 'you see a yellow algae in the river, it looks rather appeticing, what do you do?')
        activity2.add_child(sub_activity4)
        activity2.add_child(sub_activity5)
        activity2.add_child(sub_activity6)

        #------------ Watermill ------------  Done

        sub_sub_activity7_1 = Node("yes", "as you eat from the food it at first tastes very good, but after a while you start feeling ill and eventually throw up, what do you do now?")
        sub_sub_activity7_2 = Node("no", "you exit the watermill, what do you do?")
        sub_sub_activity7_1.add_child(exitactivity)
        sub_sub_activity7_2.add_child(exitactivity)

        sub_activity7 = Node("table", "the table is filled to teh brim with food, strange...  do you eat from it?")
        sub_activity7.add_child(sub_sub_activity7_1)
        sub_activity7.add_child(sub_sub_activity7_2)

        sub_sub_activity8_1 = Node("yes", "You take the rocks and put them in your backpack, what do you do?")
        sub_sub_activity8_2 = Node("no", "you exit the watermill, what do you do?")
        sub_sub_activity8_1.add_child(exitactivity)
        sub_sub_activity8_2.add_child(exitactivity)

        sub_activity8 = Node("rocks", "the pile of strange rocks all have differing colors from bright green to a dark purple, do you take the rocks?")
        sub_activity8.add_child(sub_sub_activity8_1)
        sub_activity8.add_child(sub_sub_activity8_2)

        sub_sub_activity9_1 = Node("yes", "yo take a big swig of the tankard and feel a dark smoky taste in the back of your throat and you feel a bit dizzy , what do you do?")
        sub_sub_activity9_2 = Node("no", "you leave the tankard and leave the watermill, what do you do?")
        sub_sub_activity9_1.add_child(exitactivity)
        sub_sub_activity9_2.add_child(exitactivity)

        sub_activity9 = Node("tankard", "you inspect the tankard and smell it, it smells like rum, do you taste it??")
        sub_activity9.add_child(sub_sub_activity9_1)
        sub_activity9.add_child(sub_sub_activity9_2)

        activity3 = Node("watermill", "as you enter the watermill you find some strange rocks, a table full of food and a tankard, what do you do??")
        activity3.add_child(sub_activity7)
        activity3.add_child(sub_activity8)
        activity3.add_child(sub_activity9)

        #------------ Root ------------  Done

        self.root = Node("mountain", "As you walk along the river you see some plants, algae and rocks in the river. Next to the river is an old water mill. What do you do?", move_node=False)
        self.root.add_child(activity1)
        self.root.add_child(activity2)
        self.root.add_child(activity3)

class Plain(Tile):
    def __init__(self, position):
        self.type = 'Plain'
        self.actions = {''}
        self.image = pygame.image.load('assets/plain.png')
       
       #------------ Exit ------------  Done
        
        exitactivity = Node("leave", "You walk from the large plane towards...", move_node=True)

        #------------ Gather ------------  Done

        sub_sub_activity1_1 = Node("yes", "you take the pill and it tastes really bad, nothing else, what do you do now?")
        sub_sub_activity1_2 = Node("no", "you leave the pill, what do you do?")
        sub_sub_activity1_1.add_child(exitactivity)
        sub_sub_activity1_2.add_child(exitactivity)

        sub_activity1 = Node("green pill", "you see the green pill, do you take it?")
        sub_activity1.add_child(sub_sub_activity1_1)
        sub_activity1.add_child(sub_sub_activity1_2)

        sub_sub_activity2_1 = Node("yes", "as soon as your tongue touches the pill it fades away in your mouth and you get a very strong hallucination, what do you do?")
        sub_sub_activity2_2 = Node("no", "you leave the pill, what do you do?")
        sub_sub_activity2_1.add_child(exitactivity)
        sub_sub_activity2_2.add_child(exitactivity)

        sub_activity2 = Node("purple pill", "you see the purple pill, do you take it?")
        sub_activity2.add_child(sub_sub_activity2_1)
        sub_activity2.add_child(sub_sub_activity2_2)

        sub_sub_activity3_1 = Node("yes", "you dig up a miners helmet and equip it, what do you do?")
        sub_sub_activity3_2 = Node("no", "you leave the object, what do you do?")
        sub_sub_activity3_1.add_child(exitactivity)
        sub_sub_activity3_2.add_child(exitactivity)

        sub_activity3 = Node("shiny", "you see a shiny object in the ground, do you dig it up?")
        sub_activity3.add_child(sub_sub_activity3_1)
        sub_activity3.add_child(sub_sub_activity3_2)

        activity1 = Node("gather", "you go closer to the pikes and you can see the pikes laying with something shiny in the middle, at the side of the pikes there is also a table with two different pills, what do you do?")
        activity1.add_child(sub_activity1)
        activity1.add_child(sub_activity2)
        activity1.add_child(sub_activity3)

        #------------ Research ------------  Done

        sub_sub_activity4_1 = Node("leave it", "you leave the cactus alone, what do you do?")
        sub_sub_activity4_2 = Node("pick it", "you take some cactus and put it in your backpack, what do you do then?")
        sub_sub_activity4_1.add_child(exitactivity)
        sub_sub_activity4_2.add_child(exitactivity)

        sub_activity4 = Node("feel", "you feel the cactus and its pointy, what do you do?")
        sub_activity4.add_child(sub_sub_activity4_1)
        sub_activity4.add_child(sub_sub_activity4_2)

        sub_sub_activity5_1 = Node("remove", "you take the spines out of your tongue, what do you do?")
        sub_sub_activity5_2 = Node("ignore", "you ignore the spines, what do you do?")
        sub_sub_activity5_1.add_child(exitactivity)
        sub_sub_activity5_2.add_child(exitactivity)

        sub_activity5 = Node("lick", "as you lick the cactus you get a load of the spines stuck on your tongue, what do you do?")
        sub_activity5.add_child(sub_sub_activity5_1)
        sub_activity5.add_child(sub_sub_activity5_2)

        sub_sub_activity6_1 = Node("eat more", "you eat more for some reason and the pain you were in is now gone, what do you do?")
        sub_sub_activity6_2 = Node("leave it", "you leave the cacti and your mouth now stings, what do you do?")
        sub_sub_activity6_1.add_child(exitactivity)
        sub_sub_activity6_2.add_child(exitactivity)

        sub_activity6 = Node("bite", "you take a bite of the and your mouth is now in extreme pain, what do you do?")
        sub_activity6.add_child(sub_sub_activity6_1)
        sub_activity6.add_child(sub_sub_activity6_2)

        activity2 = Node("research", 'you see a cactus, it looks rather pointy, what do you do?')
        activity2.add_child(sub_activity4)
        activity2.add_child(sub_activity5)
        activity2.add_child(sub_activity6)

        #------------ Watermill ------------  Done

        sub_sub_activity7_1 = Node("yes", "you put on your new kicks, what do you do now?")
        sub_sub_activity7_2 = Node("no", "you exit the shack, what do you do?")
        sub_sub_activity7_1.add_child(exitactivity)
        sub_sub_activity7_2.add_child(exitactivity)

        sub_activity7 = Node("shoes", "the shoes seem old but should function, do you use them?")
        sub_activity7.add_child(sub_sub_activity7_1)
        sub_activity7.add_child(sub_sub_activity7_2)

        sub_sub_activity8_1 = Node("yes", "You take the coins and put them in your backpack, what do you do?")
        sub_sub_activity8_2 = Node("no", "you exit the shack, what do you do?")
        sub_sub_activity8_1.add_child(exitactivity)
        sub_sub_activity8_2.add_child(exitactivity)

        sub_activity8 = Node("shiny", "those are coins on the table, do you take the coins?")
        sub_activity8.add_child(sub_sub_activity8_1)
        sub_activity8.add_child(sub_sub_activity8_2)

        sub_sub_activity9_1 = Node("yes", "you take a big hefty swig of the water and feel great, what do you do?")
        sub_sub_activity9_2 = Node("no", "you leave the bucket and leave the shack a bit more thirsty, what do you do?")
        sub_sub_activity9_1.add_child(exitactivity)
        sub_sub_activity9_2.add_child(exitactivity)

        sub_activity9 = Node("bucket", "you inspect the bucket, it is filled of water, do you taste it??")
        sub_activity9.add_child(sub_sub_activity9_1)
        sub_activity9.add_child(sub_sub_activity9_2)

        activity3 = Node("shack", "as you enter the shack you see a bucket, something shiny at a table and some shoes, what do you do??")
        activity3.add_child(sub_activity7)
        activity3.add_child(sub_activity8)
        activity3.add_child(sub_activity9)

        #------------ Root ------------  Done

        self.root = Node("plain", "You walk along the flat surface of the dry plain and see an old shack, a cactus and some pikes in the ground. What do you do?", move_node=False)
        self.root.add_child(activity1)
        self.root.add_child(activity2)
        self.root.add_child(activity3)