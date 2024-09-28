from monteprediction.truth import get_most_recent_truth
from monteprediction.scoring import compute_score

from monteprediction.verification import get_verification_status
import os
from dotenv import load_dotenv

load_dotenv()

print(get_verification_status(email=os.getenv("YOUR_EMAIL")))


z = get_most_recent_truth()
print({'z':z})



# score = compute_score(samples=df.values, z=z)
# print(f"Score using your samples above last week: {score}")