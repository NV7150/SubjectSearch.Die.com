module Model exposing (..)

import Url
import Browser
import Browser.Navigation as Nav
import Url.Parser exposing (Parser, oneOf, s, map, top, (</>))
import Utils.Lang exposing (Language)
import Utils.Lang exposing (Language(..))
import Aspect.Model

-- MSG

type Msg
    = UrlRequested Browser.UrlRequest
    | UrlChanged Url.Url
    | AspectMsg Aspect.Model.Msg


-- Model

type alias RootModel =
    { key : Nav.Key
    , url : Url.Url
    , lang: Language
    , aspectPage: Aspect.Model.AspectModel
    }


type Route
    = Home
    | AspectIndex


routeParser : Parser ((Route, Language) -> a) a
routeParser =
    oneOf
        [ map (Home, JA_JP) top
        , map (Home, EN_US) (s "en")
        , map (AspectIndex, JA_JP) (s "aspect")
        , map (AspectIndex, EN_US) (s "en" </> (s "aspect") )
        ]
