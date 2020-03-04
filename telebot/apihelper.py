import json
# import requests

# import telebot
from telebot import types
from telebot import util

# proxy = None
# format_header_param = None

# API_URL = None
# FILE_URL = None


def get_me(token):
    method_url = r'getMe'
    return _make_request(token, method_url)


def get_file(token, file_id):
    method_url = r'getFile'
    return _make_request(token, method_url, params={'file_id': file_id})


def get_file_url(token, file_id):
    if FILE_URL is None:
        return "https://api.telegram.org/file/bot{0}/{1}".format(token, get_file(token, file_id)['file_path'])
    else:
        return FILE_URL.format(token, get_file(token, file_id)['file_path'])
 

def download_file(token, file_path):
    if FILE_URL is None:
        url =  "https://api.telegram.org/file/bot{0}/{1}".format(token, file_path)
    else:
        url =  FILE_URL.format(token, file_path)
        
    result = _get_req_session().get(url, proxies=proxy)
    if result.status_code != 200:
        msg = 'The server returned HTTP {0} {1}. Response body:\n[{2}]' \
            .format(result.status_code, result.reason, result.text)
        raise ApiException(msg, 'Download file', result)
    return result.content


def send_message(token, chat_id, text, disable_web_page_preview=None, reply_to_message_id=None, reply_markup=None,
                 parse_mode=None, disable_notification=None, timeout=None):
    """
    Use this method to send text messages. On success, the sent Message is returned.
    :param token:
    :param chat_id:
    :param text:
    :param disable_web_page_preview:
    :param reply_to_message_id:
    :param reply_markup:
    :param parse_mode:
    :param disable_notification:
    :return:
    """
    method_url = r'sendMessage'
    payload = {'chat_id': str(chat_id), 'text': text}
    if disable_web_page_preview:
        payload['disable_web_page_preview'] = disable_web_page_preview
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if timeout:
        payload['connect-timeout'] = timeout
    # return _make_request(token, method_url, params=payload, method='post')
    return payload


def send_photo(token, chat_id, photo, caption=None, reply_to_message_id=None, reply_markup=None,
               parse_mode=None, disable_notification=None):
    method_url = r'sendPhoto'
    payload = {'chat_id': chat_id}
    files = None
    if not util.is_string(photo):
        files = {'photo': photo}
    else:
        payload['photo'] = photo
    if caption:
        payload['caption'] = caption
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if disable_notification:
        payload['disable_notification'] = disable_notification
    # return _make_request(token, method_url, params=payload, files=files, method='post')
    return payload


def send_media_group(token, chat_id, media, disable_notification=None, reply_to_message_id=None):
    method_url = r'sendMediaGroup'
    media_json, files = _convert_input_media_array(media)
    payload = {'chat_id': chat_id, 'media': media_json}
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    #return _make_request(token, method_url, params=payload, method='post' if files else 'get',
    #                     files=files if files else None)
    return payload


def send_location(token, chat_id, latitude, longitude, live_period=None, reply_to_message_id=None, reply_markup=None,
                  disable_notification=None):
    method_url = r'sendLocation'
    payload = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude}
    if live_period:
        payload['live_period'] = live_period
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if disable_notification:
        payload['disable_notification'] = disable_notification
    # return _make_request(token, method_url, params=payload)
    return payload


def edit_message_live_location(token, latitude, longitude, chat_id=None, message_id=None,
                               inline_message_id=None, reply_markup=None):
    method_url = r'editMessageLiveLocation'
    payload = {'latitude': latitude, 'longitude': longitude}
    if chat_id:
        payload['chat_id'] = chat_id
    if message_id:
        payload['message_id'] = message_id
    if inline_message_id:
        payload['inline_message_id'] = inline_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return payload


def stop_message_live_location(token, chat_id=None, message_id=None,
                               inline_message_id=None, reply_markup=None):
    method_url = r'stopMessageLiveLocation'
    payload = {}
    if chat_id:
        payload['chat_id'] = chat_id
    if message_id:
        payload['message_id'] = message_id
    if inline_message_id:
        payload['inline_message_id'] = inline_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return payload


def send_venue(token, chat_id, latitude, longitude, title, address, foursquare_id=None, disable_notification=None,
               reply_to_message_id=None, reply_markup=None):
    method_url = r'sendVenue'
    payload = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude, 'title': title, 'address': address}
    if foursquare_id:
        payload['foursquare_id'] = foursquare_id
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return payload


def send_contact(token, chat_id, phone_number, first_name, last_name=None, disable_notification=None,
                 reply_to_message_id=None, reply_markup=None):
    method_url = r'sendContact'
    payload = {'chat_id': chat_id, 'phone_number': phone_number, 'first_name': first_name}
    if last_name:
        payload['last_name'] = last_name
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return payload


def send_chat_action(token, chat_id, action):
    method_url = r'sendChatAction'
    payload = {'chat_id': chat_id, 'action': action}
    return payload


def send_video(token, chat_id, data, duration=None, caption=None, reply_to_message_id=None, reply_markup=None,
               parse_mode=None, supports_streaming=None, disable_notification=None, timeout=None):
    method_url = r'sendVideo'
    payload = {'chat_id': chat_id}
    files = None
    if not util.is_string(data):
        files = {'video': data}
    else:
        payload['video'] = data
    if duration:
        payload['duration'] = duration
    if caption:
        payload['caption'] = caption
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if supports_streaming:
        payload['supports_streaming'] = supports_streaming
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if timeout:
        payload['connect-timeout'] = timeout
    return payload


def send_animation(token, chat_id, data, duration=None, caption=None, reply_to_message_id=None, reply_markup=None,
               parse_mode=None, disable_notification=None, timeout=None):
    method_url = r'sendAnimation'
    payload = {'chat_id': chat_id}
    files = None
    if not util.is_string(data):
        files = {'animation': data}
    else:
        payload['animation'] = data
    if duration:
        payload['duration'] = duration
    if caption:
        payload['caption'] = caption
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if timeout:
        payload['connect-timeout'] = timeout
    return payload


def send_voice(token, chat_id, voice, caption=None, duration=None, reply_to_message_id=None, reply_markup=None,
               parse_mode=None, disable_notification=None, timeout=None):
    method_url = r'sendVoice'
    payload = {'chat_id': chat_id}
    files = None
    if not util.is_string(voice):
        files = {'voice': voice}
    else:
        payload['voice'] = voice
    if caption:
        payload['caption'] = caption
    if duration:
        payload['duration'] = duration
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if timeout:
        payload['connect-timeout'] = timeout
    return payload


def send_video_note(token, chat_id, data, duration=None, length=None, reply_to_message_id=None, reply_markup=None,
                    disable_notification=None, timeout=None):
    method_url = r'sendVideoNote'
    payload = {'chat_id': chat_id}
    files = None
    if not util.is_string(data):
        files = {'video_note': data}
    else:
        payload['video_note'] = data
    if duration:
        payload['duration'] = duration
    if length:
        payload['length'] = length
    else:
        payload['length'] = 639  # seems like it is MAX length size
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if timeout:
        payload['connect-timeout'] = timeout
    return payload


def send_audio(token, chat_id, audio, caption=None, duration=None, performer=None, title=None, reply_to_message_id=None,
               reply_markup=None, parse_mode=None, disable_notification=None, timeout=None):
    method_url = r'sendAudio'
    payload = {'chat_id': chat_id}
    files = None
    if not util.is_string(audio):
        files = {'audio': audio}
    else:
        payload['audio'] = audio
    if caption:
        payload['caption'] = caption
    if duration:
        payload['duration'] = duration
    if performer:
        payload['performer'] = performer
    if title:
        payload['title'] = title
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if timeout:
        payload['connect-timeout'] = timeout
    return payload


def send_data(token, chat_id, data, data_type, reply_to_message_id=None, reply_markup=None, parse_mode=None,
              disable_notification=None, timeout=None, caption=None):
    method_url = get_method_by_type(data_type)
    payload = {'chat_id': chat_id}
    files = None
    if not util.is_string(data):
        files = {data_type: data}
    else:
        payload[data_type] = data
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if parse_mode and data_type == 'document':
        payload['parse_mode'] = parse_mode
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if timeout:
        payload['connect-timeout'] = timeout
    if caption:
        payload['caption'] = caption
    return payload


def get_method_by_type(data_type):
    if data_type == 'document':
        return r'sendDocument'
    if data_type == 'sticker':
        return r'sendSticker'


def kick_chat_member(token, chat_id, user_id, until_date=None):
    method_url = 'kickChatMember'
    payload = {'chat_id': chat_id, 'user_id': user_id}
    if until_date:
        payload['until_date'] = until_date
    return payload


def unban_chat_member(token, chat_id, user_id):
    method_url = 'unbanChatMember'
    payload = {'chat_id': chat_id, 'user_id': user_id}
    return payload


def restrict_chat_member(token, chat_id, user_id, until_date=None, can_send_messages=None,
                         can_send_media_messages=None, can_send_other_messages=None,
                         can_add_web_page_previews=None):
    method_url = 'restrictChatMember'
    payload = {'chat_id': chat_id, 'user_id': user_id}
    if until_date:
        payload['until_date'] = until_date
    if can_send_messages:
        payload['can_send_messages'] = can_send_messages
    if can_send_media_messages:
        payload['can_send_media_messages'] = can_send_media_messages
    if can_send_other_messages:
        payload['can_send_other_messages'] = can_send_other_messages
    if can_add_web_page_previews:
        payload['can_add_web_page_previews'] = can_add_web_page_previews

    return payload


def promote_chat_member(token, chat_id, user_id, can_change_info=None, can_post_messages=None,
                        can_edit_messages=None, can_delete_messages=None, can_invite_users=None,
                        can_restrict_members=None, can_pin_messages=None, can_promote_members=None):
    method_url = 'promoteChatMember'
    payload = {'chat_id': chat_id, 'user_id': user_id}
    if can_change_info:
        payload['can_change_info'] = can_change_info
    if can_post_messages:
        payload['can_post_messages'] = can_post_messages
    if can_edit_messages:
        payload['can_edit_messages'] = can_edit_messages
    if can_delete_messages:
        payload['can_delete_messages'] = can_delete_messages
    if can_invite_users:
        payload['can_invite_users'] = can_invite_users
    if can_restrict_members:
        payload['can_restrict_members'] = can_restrict_members
    if can_pin_messages:
        payload['can_pin_messages'] = can_pin_messages
    if can_promote_members:
        payload['can_promote_members'] = can_promote_members
    return payload


def export_chat_invite_link(token, chat_id):
    method_url = 'exportChatInviteLink'
    payload = {'chat_id': chat_id}
    return payload


# Payments (https://core.telegram.org/bots/api#payments)

def send_invoice(token, chat_id, title, description, invoice_payload, provider_token, currency, prices,
                 start_parameter, photo_url=None, photo_size=None, photo_width=None, photo_height=None,
                 need_name=None, need_phone_number=None, need_email=None, need_shipping_address=None, is_flexible=None,
                 disable_notification=None, reply_to_message_id=None, reply_markup=None, provider_data=None):
    """
    Use this method to send invoices. On success, the sent Message is returned.
    :param token: Bot's token (you don't need to fill this)
    :param chat_id: Unique identifier for the target private chat
    :param title: Product name
    :param description: Product description
    :param invoice_payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
    :param provider_token: Payments provider token, obtained via @Botfather
    :param currency: Three-letter ISO 4217 currency code, see https://core.telegram.org/bots/payments#supported-currencies
    :param prices: Price breakdown, a list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
    :param start_parameter: Unique deep-linking parameter that can be used to generate this invoice when used as a start parameter
    :param photo_url: URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
    :param photo_size: Photo size
    :param photo_width: Photo width
    :param photo_height: Photo height
    :param need_name: Pass True, if you require the user's full name to complete the order
    :param need_phone_number: Pass True, if you require the user's phone number to complete the order
    :param need_email: Pass True, if you require the user's email to complete the order
    :param need_shipping_address: Pass True, if you require the user's shipping address to complete the order
    :param is_flexible: Pass True, if the final price depends on the shipping method
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param reply_markup: A JSON-serialized object for an inline keyboard. If empty, one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button
    :param provider_data:
    :return:
    """
    method_url = r'sendInvoice'
    payload = {'chat_id': chat_id, 'title': title, 'description': description, 'payload': invoice_payload,
               'provider_token': provider_token, 'start_parameter': start_parameter, 'currency': currency,
               'prices': _convert_list_json_serializable(prices)}
    if photo_url:
        payload['photo_url'] = photo_url
    if photo_size:
        payload['photo_size'] = photo_size
    if photo_width:
        payload['photo_width'] = photo_width
    if photo_height:
        payload['photo_height'] = photo_height
    if need_name:
        payload['need_name'] = need_name
    if need_phone_number:
        payload['need_phone_number'] = need_phone_number
    if need_email:
        payload['need_email'] = need_email
    if need_shipping_address:
        payload['need_shipping_address'] = need_shipping_address
    if is_flexible:
        payload['is_flexible'] = is_flexible
    if disable_notification:
        payload['disable_notification'] = disable_notification
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if provider_data:
        payload['provider_data'] = provider_data
    return _make_request(token, method_url, params=payload)


def answer_shipping_query(token, shipping_query_id, ok, shipping_options=None, error_message=None):
    """
    If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned.
    :param token: Bot's token (you don't need to fill this)
    :param shipping_query_id: Unique identifier for the query to be answered
    :param ok: Specify True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)
    :param shipping_options: Required if ok is True. A JSON-serialized array of available shipping options.
    :param error_message: Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user.
    :return:
    """
    method_url = 'answerShippingQuery'
    payload = {'shipping_query_id': shipping_query_id, 'ok': ok}
    if shipping_options:
        payload['shipping_options'] = _convert_list_json_serializable(shipping_options)
    if error_message:
        payload['error_message'] = error_message
    return _make_request(token, method_url, params=payload)


def answer_pre_checkout_query(token, pre_checkout_query_id, ok, error_message=None):
    """
    Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.
    :param token: Bot's token (you don't need to fill this)
    :param pre_checkout_query_id: Unique identifier for the query to be answered
    :param ok: Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.
    :param error_message: Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user.
    :return:
    """
    method_url = 'answerPreCheckoutQuery'
    payload = {'pre_checkout_query_id': pre_checkout_query_id, 'ok': ok}
    if error_message:
        payload['error_message'] = error_message
    return _make_request(token, method_url, params=payload)


# Polls

def send_poll(token, chat_id, question, options, disable_notifications=False, reply_to_message_id=None, reply_markup=None):
    method_url = r'sendPoll'
    payload = {'chat_id': str(chat_id), 'question': question, 'options': _convert_list_json_serializable(options)}
    if disable_notifications:
        payload['disable_notification'] = disable_notifications
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return _make_request(token, method_url, params=payload)


def stop_poll(token, chat_id, message_id, reply_markup=None):
    method_url = r'stopPoll'
    payload = {'chat_id': str(chat_id), 'message_id': message_id}
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    return _make_request(token, method_url, params=payload)


# Format helpers

def _convert_list_json_serializable(results):
    ret = ''
    for r in results:
        if isinstance(r, types.JsonSerializable):
            ret = ret + r.to_json() + ','
    if len(ret) > 0:
        ret = ret[:-1]
    return '[' + ret + ']'


def _convert_markup(markup):
    if isinstance(markup, types.JsonSerializable):
        return markup.to_json()
    return markup


def _convert_input_media(media):
    if isinstance(media, types.InputMedia):
        return media._convert_input_media()
    return None, None


def _convert_input_media_array(array):
    media = []
    files = {}
    for input_media in array:
        if isinstance(input_media, types.InputMedia):
            media_dict = input_media.to_dic()
            if media_dict['media'].startswith('attach://'):
                key = media_dict['media'].replace('attach://', '')
                files[key] = input_media.media
            media.append(media_dict)
    return json.dumps(media), files


def _no_encode(func):
    def wrapper(key, val):
        if key == 'filename':
            return u'{0}={1}'.format(key, val)
        else:
            return func(key, val)

    return wrapper