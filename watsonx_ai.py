from ibm_watsonx_ai.foundation_models import ModelInference
import os

def get_credentials():
	return {
		'url':os.getenv("IBM_CLOUD_URL", None),
		"apikey" : os.getenv("WATSONX_API_KEY", None) 
	}

def generate_response(prompt,model):
	model_id = model
	parameters = {
    	"decoding_method": "greedy",
    	"max_new_tokens": 8096,
    	"min_new_tokens": 0,
    	"repetition_penalty": 1,
		# "temperature":0,
		# "random_seed": 42
	}
	# parameters = {
    # "frequency_penalty": 0,
    # "max_tokens": 2000,
    # "presence_penalty": 0,
    # "temperature": 0,
    # "top_p": 1
	# }
	project_id = os.getenv("PROJECT_ID")
	model = ModelInference(
			model_id = model_id,
			params = parameters,
			credentials = get_credentials(),
			project_id = project_id
			)
	

	print("Submitting generation request...")
	generated_response = model.generate_text(prompt=prompt, guardrails=False)
	return generated_response
