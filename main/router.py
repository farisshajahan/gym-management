from rest_framework.routers import SimpleRouter

from main.views import SignUpView
from main.viewsets import ProgrammeViewset

router = SimpleRouter()
router.register("programme", ProgrammeViewset)
