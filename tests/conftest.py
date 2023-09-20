import pytest
import random

@pytest.fixture(autouse=True, scope='session')
def set_seed():
    """
    Note that in BSR we use random functions from the random module instead of np.random
    """
    random.seed(2023)
