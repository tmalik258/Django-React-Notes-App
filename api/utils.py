from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer


def getNotesList(request):
    notes = Note.objects.all().order_by("-updated")
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


def getNoteDetail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except ObjectDoesNotExist:
        content = {"please move along": "nothing to see here"}
        return Response(content, status=status.HTTP_204_NO_CONTENT)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def createNote(request):
    data = request.data
    note = Note.objects.create(body=data["body"])
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def updateNote(request, pk):
    try:
        note = Note.objects.get(pk=pk)
        data = request.data
    except ObjectDoesNotExist:
        content = {"please move along": "nothing to see here"}
        return Response(content, status=status.HTTP_204_NO_CONTENT)

    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


def deleteNote(request, pk):
    try:
        note = Note.objects.get(pk=pk)
        note.delete()
    except ObjectDoesNotExist:
        content = {"please move along": "nothing to see here"}
        return Response(content, status=status.HTTP_204_NO_CONTENT)

    return Response("Note was Deleted!")
