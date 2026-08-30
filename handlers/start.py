from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    # Styled buttons with Kurigram enums.ButtonStyle
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "💙 Open Portal", 
                url="https://t.me/example_username?startgroup=start", 
                style=enums.ButtonStyle.PRIMARY
            )
        ],
        [
            InlineKeyboardButton(
                "💚 Success Action", 
                callback_data="success_click", 
                style=enums.ButtonStyle.SUCCESS
            ),
            InlineKeyboardButton(
                "❤️ Danger Action", 
                callback_data="danger_click", 
                style=enums.ButtonStyle.DANGER
            )
        ]
    ])

    await message.reply_text(
        f"<b>Welcome, {message.from_user.mention}!</b>\n\nChoose an option below:",
        reply_markup=keyboard
    )

@Client.on_callback_query(filters.regex("^(success_click|danger_click)$"))
async def callback_handler(client, callback_query):
    data = callback_query.data
    if data == "success_click":
        await callback_query.answer("💚 Success: Action processed successfully!", show_alert=True)
    elif data == "danger_click":
        await callback_query.answer("❤️ Danger: Action warning triggered!", show_alert=True)
