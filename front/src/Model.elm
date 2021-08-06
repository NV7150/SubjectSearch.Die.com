module Model exposing (..)

import Url
import Browser
import Browser.Navigation as Nav
import Url.Parser exposing (Parser, oneOf, s, map, top, (</>))
import Utils.Lang exposing (Language)
import Utils.Lang exposing (Language(..))


-- MSG

type Msg
    = UrlRequested Browser.UrlRequest
    | UrlChanged Url.Url


-- Model

type alias RootModel =
    { key : Nav.Key
    , url : Url.Url
    , lang: Language
    }


type Route
    = Home
    | GenreIndex


routeParser : Parser ((Route, Language) -> a) a
routeParser =
    oneOf
        [ map (Home, JA_JP) top
        , map (Home, EN_US) (s "en")
        , map (GenreIndex, JA_JP) (s "genre")
        , map (GenreIndex, EN_US) (s "en" </> (s "genre") )
        ]
