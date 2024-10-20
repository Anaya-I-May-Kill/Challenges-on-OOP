class flashcard:
    
    def __init__(self , word, meaning):
        self.word = word
        self.meaning = meaning
        
    def __str__(self):
        return self.word+' ( '+self.meaning+')'
    
flash = []
print("welcome to flash applications")

while(True):
    word = input("Enter the name you wanna add : ")
    meaning = input("Enter the meaning : ")
    
    flash.append(   flashcard(word, meaning))   
    option = int(input("Enter 0 to  add another flashcard otherwise enter 1"))
    
    if(option):
        break
    
print("\nYour flashcards:")
for i in flash:
    print(">" , i)