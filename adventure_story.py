# Alex Williams
# 9/10/2024
# f-String Adventure Story

'''
Directions:

1. Update the comment block at the top of this script.

2. Use the Python `input( )` function to prompt (ask) the user for three pieces of information:

     - the hero's first name
     - the setting of the story (e.g., forest, desert, cave system)
     - the object the hero finds while on his/her adventure

3. Assign each piece of information collected to a variable with a short, specific name.

4. Declare (create) a variable named `story` and assign to it the `f-string` that is your adventure story

5. Use the `print( )` function to display your adventure story on the screen.

6. Execute (run) your script in Visual Studio Code and correct any errors.
'''


hero_name = input('Please enter your first name:\n')
setting = input('where does your adventure story take place?:\n')
heroic_item = input('what item does your hero find on their adventure?\n')
print (f'the great hero {hero_name} saved {setting} with a {heroic_item} from the evil forces')
