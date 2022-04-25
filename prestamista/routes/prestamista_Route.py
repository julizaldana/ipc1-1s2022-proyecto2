from flask import Blueprint, jsonify, request
from db.database import libraryDatabase
from prestamista.models.prestamista_Model import Prestamista