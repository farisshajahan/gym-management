from rest_framework.routers import SimpleRouter

from main.viewsets import ProgrammeViewset

router = SimpleRouter()
router.register("programme", ProgrammeViewset)
