module Main exposing (main)

import Browser
import Browser.Navigation as Nav
import Html exposing (..)
import Html.Attributes exposing (..)
import Url

import Model exposing (RootModel, Msg(..))
import Model exposing (Route(..))
import View exposing (view)
import Utils.Lang exposing (Language(..))
import Aspect.Model
import Aspect.Aspect

import Url.Parser


main : Program () RootModel Msg
main =
    Browser.application
        { init = init
        , view = view
        , update = update
        , subscriptions = subscriptions
        , onUrlRequest = UrlRequested
        , onUrlChange = UrlChanged
        }


init : flags -> Url.Url -> Nav.Key -> ( RootModel, Cmd Msg )
init flags url key =
    ( RootModel key url JA_JP Aspect.Model.fakeModel , Cmd.none )


update : Msg -> RootModel -> ( RootModel, Cmd Msg )
update msg model =
    case msg of
        UrlRequested urlRequest ->
            case urlRequest of
                Browser.Internal url ->
                    ( model, Nav.pushUrl model.key (Url.toString url) )

                Browser.External href ->
                    ( model, Nav.load href )

        UrlChanged url ->
            let
                lang =
                    case Url.Parser.parse Model.routeParser url of
                        Just (_, l) ->
                            l
                        Nothing ->
                            model.lang
            in
            ( { model | url = url, lang = lang }
            , Cmd.none
            )
        
        AspectMsg subMsg ->
            let
                (subModel, subCmd) =
                    Aspect.Aspect.update subMsg model.aspectPage
            in
            ( { model | aspectPage = subModel }
            , Cmd.map AspectMsg subCmd
            )


subscriptions : RootModel -> Sub Msg
subscriptions model =
    Sub.none

