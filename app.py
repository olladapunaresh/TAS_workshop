from watsonx_ai import generate_response
import dotenv

dotenv.load_dotenv()



prompt="""
You are an assistant who greets users with a joke and welcome them to IBM TAS workshop

output:


"""



if __name__ == "__main__":

    '''
    
    '''

    model="ibm/granite-3-8b-instruct"

    response = generate_response(prompt, model)

    print(response)  # or save to file if preferred








