class BaseGenChapter:
    def __init__(*args, **kwargs):
        pass
    
    def _call(self, *args, **kwargs) -> str:
        raise NotImplementedError("_call not Implement yet")
    
    def call(self, *args, **kwargs) -> str:
        return self._call(*args, **kwargs)