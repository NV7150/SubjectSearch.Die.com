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
import Subject.Subject
import Subject.Model

import Url.Parser


main : Program () RootModel Model.Msg
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
    let
        model =
            RootModel
                key url JA_JP
                Aspect.Model.fakeModel
                Subject.Model.fakeModel
    in
    initCmd model


update : Model.Msg -> RootModel -> ( RootModel, Cmd Model.Msg )
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
                        Just (Home l) -> l
                        Just (AspectIndex l) -> l
                        Just (SubjectPage l _) -> l
                        Nothing ->
                            model.lang
                (newModel, newCmd) =
                    initCmd { model | url = url, lang = lang }
            in
            (newModel, newCmd)
        
        AspectMsg subMsg ->
            let
                (subModel, subCmd) =
                    Aspect.Aspect.update subMsg model.aspectPage
            in
            ( { model | aspectPage = subModel }
            , Cmd.map AspectMsg subCmd
            )
        
        SubjectMsg subMsg ->
            let
                (subModel, subCmd) =
                    Subject.Subject.update subMsg model.subjectPage
            in
            ( { model | subjectPage = subModel }
            , Cmd.map SubjectMsg subCmd
            )


subscriptions : RootModel -> Sub Msg
subscriptions model =
    Sub.none



-- FUNC

initCmd : RootModel -> (RootModel, Cmd Msg)
initCmd model =
    case Url.Parser.parse Model.routeParser model.url of
        Just (SubjectPage _ filter) ->
            let
                (m, c) =
                    Subject.Subject.update (Subject.Model.InitMsg model.url) model.subjectPage
            in
            ( { model | subjectPage = m}
            , Cmd.map SubjectMsg c
            )
        _ ->
            (model, Cmd.none)

