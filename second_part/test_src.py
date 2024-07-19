import pytest
import src
from src import CacheDecorator, AccessWebsite

################# Example usage for http_request #################
result = src.http_request()
print(result)

################# Example usage for first_day_of_last_week #################
formatted_date = src.first_day_of_last_week()
print(formatted_date)

################# Test class for CacheDecorator #################
class TestCacheDecorator:
    
    def setup_method(self):
        self.decorator = CacheDecorator()
        
    def test_cache_stores_results(self):
        @self.decorator
        def add(a, b):
            return a + b
        
        result1 = add(1, 2)
        result2 = add(1, 2)
        assert result1 == 3
        assert result1 == result2, "The cached result should be returned for the same parameters"
    
    def test_cache_different_arguments(self):
        @self.decorator
        def multiply(a, b):
            return a * b
        
        result1 = multiply(2, 3)
        result2 = multiply(3, 3)
        assert result1 == 6
        assert result2 == 9
        assert result1 != result2, "Different arguments should produce different results"
    
    def test_cache_with_multiple_parameters(self):
        @self.decorator
        def subtract(a, b, c):
            return a - b - c
        
        result1 = subtract(10, 5, 2)
        result2 = subtract(10, 5, 2)
        assert result1 == 3
        assert result1 == result2, "The cached result should be returned for the same parameters"
    
    def test_cache_with_no_parameters(self):
        @self.decorator
        def constant():
            return 42
        
        result1 = constant()
        result2 = constant()
        assert result1 == 42
        assert result1 == result2, "The cached result should be returned for no parameters"
    
    def test_cache_not_caching_properly(self):
        @self.decorator
        def power(a, b):
            return a ** b
        
        result1 = power(2, 3)
        result2 = power(2, 4)
        assert result1 == 8
        assert result2 == 16
        assert result1 != result2, "Different arguments should produce different results"
    
    def test_cache_same_first_argument(self):
        @self.decorator
        def concat(a, b):
            return a + b
        
        result1 = concat("Hello", " World")
        result2 = concat("Hello", " there")
        assert result1 == "Hello World"
        assert result2 == "Hello there"
        assert result1 != result2, "Different second arguments should produce different results"

def test_access_website():
    website = AccessWebsite()
    website.login(username="admin", password="admin")
    assert website.access_website() == "Success"
    website2 = AccessWebsite()
    website2.login(username="test", password="test")
    with pytest.raises(Exception):
        website2.access_website()

def test_access_website_not_logged_in():
    website = AccessWebsite()
    with pytest.raises(src.NotLoggedInException):
        website.access_website()

if __name__ == "__main__":
    pytest.main()