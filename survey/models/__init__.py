# -*- coding: utf-8 -*-

"""
Permit to import everything from survey.models without knowing the details.
"""

from .answer import Answer
from .category import Category
from .question import Question
from .response import Response
from .survey import Survey
from .image import Image
from .insect import Insect

__all__ = ["Category", "Answer", "Category", "Response", "Survey", "Question", "Image", "Insect"]
