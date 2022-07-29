import Yolo as model
import Amazon
import Email

if __name__ == "__main__":
    
    #Save all found objects by the ML model
    found_objects = model.set_model()

    #Check for all the objects and if they are
    #missing, place an order through Amazon
    for object in found_objects:
        
        print(object)
    
        if object == 'None':
            Amazon.AutoBuy()
            Email.SendEmail()