# <?php

# /**
#  * Hypertext Transfer Protocol (HTTP) Method Registry
#  *
#  * http://www.iana.org/assignments/http-methods/http-methods.xhtml
#  */

# namespace Unirest;

# interface Method
# {
#     // RFC7231
#     const GET = 'GET';
#     const HEAD = 'HEAD';
#     const POST = 'POST';
#     const PUT = 'PUT';
#     const DELETE = 'DELETE';
#     const CONNECT = 'CONNECT';
#     const OPTIONS = 'OPTIONS';
#     const TRACE = 'TRACE';

#     // RFC3253
#     const BASELINE = 'BASELINE';

#     // RFC2068
#     const LINK = 'LINK';
#     const UNLINK = 'UNLINK';

#     // RFC3253
#     const MERGE = 'MERGE';
#     const BASELINECONTROL = 'BASELINE-CONTROL';
#     const MKACTIVITY = 'MKACTIVITY';
#     const VERSIONCONTROL = 'VERSION-CONTROL';
#     const REPORT = 'REPORT';
#     const CHECKOUT = 'CHECKOUT';
#     const CHECKIN = 'CHECKIN';
#     const UNCHECKOUT = 'UNCHECKOUT';
#     const MKWORKSPACE = 'MKWORKSPACE';
#     const UPDATE = 'UPDATE';
#     const LABEL = 'LABEL';

#     // RFC3648
#     const ORDERPATCH = 'ORDERPATCH';

#     // RFC3744
#     const ACL = 'ACL';

#     // RFC4437
#     const MKREDIRECTREF = 'MKREDIRECTREF';
#     const UPDATEREDIRECTREF = 'UPDATEREDIRECTREF';

#     // RFC4791
#     const MKCALENDAR = 'MKCALENDAR';

#     // RFC4918
#     const PROPFIND = 'PROPFIND';
#     const LOCK = 'LOCK';
#     const UNLOCK = 'UNLOCK';
#     const PROPPATCH = 'PROPPATCH';
#     const MKCOL = 'MKCOL';
#     const COPY = 'COPY';
#     const MOVE = 'MOVE';

#     // RFC5323
#     const SEARCH = 'SEARCH';

#     // RFC5789
#     const PATCH = 'PATCH';

#     // RFC5842
#     const BIND = 'BIND';
#     const UNBIND = 'UNBIND';
#     const REBIND = 'REBIND';
# }


class Method:
    # RFC7231
    GET = 'GET'
    HEAD = 'HEAD'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    CONNECT = 'CONNECT'
    OPTIONS = 'OPTIONS'
    TRACE = 'TRACE'

    # RFC3253
    BASELINE = 'BASELINE'

    # RFC2068
    LINK = 'LINK'
    UNLINK = 'UNLINK'

    # RFC3253
    MERGE = 'MERGE'
    BASELINECONTROL = 'BASELINE-CONTROL'
    MKACTIVITY = 'MKACTIVITY'
    VERSIONCONTROL = 'VERSION-CONTROL'
    REPORT = 'REPORT'
    CHECKOUT = 'CHECKOUT'
    CHECKIN = 'CHECKIN'
    UNCHECKOUT = 'UNCHECKOUT'
    MKWORKSPACE = 'MKWORKSPACE'
    UPDATE = 'UPDATE'
    LABEL = 'LABEL'

    # RFC3648
    ORDERPATCH = 'ORDERPATCH'

    # RFC3744
    ACL = 'ACL'

    # RFC4437
    MKREDIRECTREF = 'MKREDIRECTREF'
    UPDATEREDIRECTREF = 'UPDATEREDIRECTREF'

    # RFC4791
    MKCALENDAR = 'MKCALENDAR'

    # RFC4918
    PROPFIND = 'PROPFIND'
    LOCK = 'LOCK'
    UNLOCK = 'UNLOCK'
    PROPPATCH = 'PROPPATCH'
    MKCOL = 'MKCOL'
    COPY = 'COPY'
    MOVE = 'MOVE'

    # RFC5323
    SEARCH = 'SEARCH'

    # RFC5789
    PATCH = 'PATCH'

    # RFC5842
    BIND = 'BIND'
    UNBIND = 'UNBIND'
    REBIND = 'REBIND'

