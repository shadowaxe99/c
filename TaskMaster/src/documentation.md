# TaskMaster Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Dependencies](#dependencies)
5. [Shared Dependencies](#shared-dependencies)
6. [File Structure](#file-structure)

## Introduction
TaskMaster is a MacOS AI Agent application designed to streamline and enhance user productivity by managing tasks and serving as a central hub for AI management.

## Features
1. Task Management
2. AI Agent Management
3. Cursor Control
4. AI Hub/Wallet
5. Auto Sync
6. Quick Sync
7. Export
8. Search and Highlight
9. Language and Style Selection
10. Utilities
11. Newsletter

## Tech Stack
- Frontend: Swift (using SwiftUI for UI design)
- Backend: Python (For AI and task management functionality)
- Database: SQLite (For local data storage)
- AI: PyTorch (For AI model implementation)

## Dependencies
1. MacOS system for deployment.
2. Swift and Python compilers for code compilation.
3. PyTorch library for AI functionalities.
4. SQLite database for local data storage.
5. Access to system resources (e.g., system notifications, cursor control, etc.) may require user permissions.

## Shared Dependencies
1. Variables: task_list, ai_agents, cursor_position, ai_wallet, sync_status, export_data, search_query, language_style, utility_settings, newsletter_archive.
2. Data Schemas: TaskSchema, AgentSchema, WalletSchema, ExportSchema, NewsletterSchema.
3. DOM Element IDs: taskList, aiAgentList, cursorControl, aiWallet, syncStatus, exportData, searchInput, languageStyleSelection, utilitySettings, newsletterArchive.
4. Message Names: TaskUpdate, AgentUpdate, CursorUpdate, WalletUpdate, SyncUpdate, ExportUpdate, SearchUpdate, LanguageStyleUpdate, UtilityUpdate, NewsletterUpdate.
5. Function Names: manageTasks, manageAgents, controlCursor, manageWallet, autoSync, quickSync, exportData, searchHighlight, selectLanguageStyle, manageUtilities, updateNewsletter.

## File Structure
- TaskMaster/
  - src/
    - main.py
    - task_management.py
    - ai_agent_management.py
    - cursor_control.py
    - ai_wallet.py
    - auto_sync.py
    - quick_sync.py
    - export.py
    - search_highlight.py
    - language_style_selection.py
    - utilities.py
    - newsletter.py
    - frontend.swift
    - backend.py
    - database.sqlite
    - ai_model.py
    - dependencies.py
    - documentation.md
    - git_push.py
  - FINISHED/
    - taskmaster_app.py