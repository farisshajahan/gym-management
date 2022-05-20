from rest_framework.routers import SimpleRouter

from main.viewsets import ProgrammeViewset, TrainerViewset

router = SimpleRouter()
router.register("programme", ProgrammeViewset)
router.register("trainer", TrainerViewset)
