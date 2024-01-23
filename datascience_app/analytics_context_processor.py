# analytics_context_processor.py
import os

def google_analytics(request):
    return {
        'GA_TRACKING_ID': os.getenv("GOOGLE_ANALYTICS_ID"),
    }