from IPython.core.debugger import Tracer

# Usage example:
# import ipdb; ipdb.set_trace()
# so yes, Tracer() returns a callable
set_trace = Tracer(colors="Linux")

