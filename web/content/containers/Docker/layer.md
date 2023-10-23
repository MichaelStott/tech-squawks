Layers capture a particular amount of work done in building the image

Docker caches these layers on build attempts for instance, building the following image:

If we modify the echo output to some other string, then docker has the previous layers from updating the dependencies and doesn't redownload the data.

However, if we change the ordering of commands and rerun rebuild

because a previous layer has changed, Docker needs to rebuild any following layers in the event something had changed.

Because of this, dependencies generally speaking should be downloaded fetched first in the dockerfile before project specific code is copied over.
