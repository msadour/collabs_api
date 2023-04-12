from source.endpoints.account.models import Account
from source.endpoints.chat.models import Chat, Message


def create_or_get_chat(author: Account, receiver: Account) -> Chat:
    current_chat = Chat.objects.filter(participants__id=author.id).intersection(
        Chat.objects.filter(participants__id=receiver.id)
    )
    if len(current_chat) == 0:
        chat: Chat = Chat.objects.create()
        chat.participants.add(author)
        chat.participants.add(receiver)
    elif len(current_chat) > 1:
        raise Exception("Error, you cannot have many chats with the same user")
    else:
        chat: Chat = Chat.objects.get(id=current_chat[0].id)

    return chat


def send_message(content: str, author: Account, chat: Chat) -> None:
    Message.objects.create(content=content, author=author, chat=chat)
